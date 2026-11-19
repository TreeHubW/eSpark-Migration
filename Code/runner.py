from datetime import datetime, timedelta, timezone
from pyspark.sql import functions as F
from KPIs.POA_Irradiation import POA_Irradiation

RAW_TABLE = "espark_consumer_group.us_performance.measurement_with_context"
MAPPING_TABLE = "Mapping_Table"
OUTPUT_TABLE = "POA_Irradiation"


class Runner:
    """Run the currently implemented POA calculation for configured plants."""

    kpi_registry = {"POA_Irradiation": POA_Irradiation}

    def __init__(
        self,
        spark,
        raw_table=RAW_TABLE,
        mapping_table=MAPPING_TABLE,
        output_table=OUTPUT_TABLE,
        read_padding_minutes=60,
    ):
        self.spark = spark
        self.raw_table = raw_table
        self.mapping_table = mapping_table
        self.output_table = output_table
        if read_padding_minutes < 0:
            raise ValueError("read_padding_minutes cannot be negative")
        self.read_padding_minutes = read_padding_minutes

    def run(self, start_time, end_time):
        """Recompute and replace results in [start_time, end_time), using UTC."""
        start = self._parse_timestamp(start_time)
        end = self._parse_timestamp(end_time)
        if start >= end:
            raise ValueError("start_time must be earlier than end_time")

        mapping = self.spark.table(self.mapping_table)
        required_mapping_columns = {
            "plant_id",
            "calculation",
            "specific_measurement_id",
            "specific_measurement_name",
        }
        missing_mapping_columns = required_mapping_columns.difference(mapping.columns)
        if missing_mapping_columns:
            raise ValueError(
                "Mapping table is missing required columns: "
                + ", ".join(sorted(missing_mapping_columns))
            )

        mapping_rows = (
            mapping.select(
                "plant_id",
                "calculation",
                "specific_measurement_id",
                "specific_measurement_name",
            )
            .distinct()
            .collect()
        )
        if not mapping_rows:
            raise ValueError("Mapping table contains no configured measurements")

        grouped_mappings = {}
        for row in mapping_rows:
            plant_id = row["plant_id"]
            calculation = row["calculation"]
            measurement_id = row["specific_measurement_id"]
            measurement_column = row["specific_measurement_name"]
            if (
                not plant_id
                or not calculation
                or not measurement_id
                or not measurement_column
            ):
                raise ValueError(f"Invalid mapping row: {row}")
            if calculation not in self.kpi_registry:
                raise ValueError(
                    f"Unsupported calculation in mapping table: {calculation}"
                )
            grouped_mappings.setdefault((plant_id, calculation), []).append(
                (measurement_column, measurement_id)
            )

        raw = self.spark.table(self.raw_table)
        required_raw_columns = {
            "id",
            "plant_id",
            "timestamp",
            "value",
        }
        missing_raw_columns = required_raw_columns.difference(raw.columns)
        if missing_raw_columns:
            raise ValueError(
                "Raw table is missing required columns: "
                + ", ".join(sorted(missing_raw_columns))
            )

        padded_start = start - timedelta(minutes=self.read_padding_minutes)
        padded_end = end + timedelta(minutes=self.read_padding_minutes)
        raw = raw.filter(
            (F.col("timestamp") >= F.lit(padded_start))
            & (F.col("timestamp") < F.lit(padded_end))
        )

        outputs = []
        for (plant_id, calculation), measurements in grouped_mappings.items():
            matches = None
            mapped_keys = []
            for measurement_column, measurement_id in measurements:
                if measurement_column not in raw.columns:
                    raise ValueError(
                        f"Mapping column '{measurement_column}' is not present "
                        f"in raw table '{self.raw_table}'"
                    )
                escaped_column = measurement_column.replace("`", "``")
                column = F.col(f"`{escaped_column}`").cast("string")
                match = column == F.lit(str(measurement_id))
                matches = match if matches is None else matches | match
                mapped_keys.append(F.when(match, column))

            mapped_key = (
                mapped_keys[0] if len(mapped_keys) == 1 else F.coalesce(*mapped_keys)
            )
            mapped_raw = (
                raw.filter((F.col("plant_id") == plant_id) & matches)
                .withColumn("key", mapped_key)
            )
            kpi = self.kpi_registry[calculation]()
            calculated = kpi.calculate(mapped_raw)
            value_column = kpi.rollup_columns[0]
            if value_column not in calculated.columns:
                raise ValueError(
                    f"{calculation}.calculate() did not produce '{value_column}'"
                )

            result = (
                calculated.filter(
                    (F.col("timestamp") >= F.lit(start))
                    & (F.col("timestamp") < F.lit(end))
                )
                .groupBy("plant_id", "key", "timestamp")
                .agg(
                    F.avg(F.col(value_column)).cast("double").alias("value"),
                    F.max("bad_flag").cast("int").alias("bad_flag"),
                )
                .withColumn("calculation", F.lit(calculation))
                .select(
                    "plant_id", "timestamp", "calculation", "value", "bad_flag", "key"
                )
            )
            outputs.append(result)

        output = outputs[0]
        for result in outputs[1:]:
            output = output.unionByName(result)

        replace_condition = (
            f"`timestamp` >= {self._sql_timestamp(start)} "
            f"AND `timestamp` < {self._sql_timestamp(end)}"
        )
        (
            output.write.format("delta")
            .mode("overwrite")
            .option("replaceWhere", replace_condition)
            .saveAsTable(self.output_table)
        )
        return output

    @staticmethod
    def _parse_timestamp(value):
        if not isinstance(value, str):
            raise TypeError("Timestamps must be ISO-8601 strings")
        try:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError as exc:
            raise ValueError(f"Invalid ISO-8601 timestamp: {value}") from exc
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc).replace(tzinfo=None)

    @staticmethod
    def _sql_timestamp(value):
        return "TIMESTAMP '" + value.strftime("%Y-%m-%d %H:%M:%S.%f") + "'"