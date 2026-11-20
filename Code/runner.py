import logging
from datetime import datetime, timedelta, timezone

from pyspark.sql import functions as F

import processing as pro
from KPIs.POA_Irradiation import POA_Irradiation


logger = logging.getLogger(__name__)

# Unity Catalog location (catalog.schema) for all project tables.
SCHEMA = "espark_consumer_group.us_performance"
RAW_TABLE = f"{SCHEMA}.measurement_with_context"
MAPPING_TABLE = f"{SCHEMA}.Mapping_Table"
OUTPUT_TABLE = f"{SCHEMA}.POA_Irradiation"


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
        # All window boundaries are UTC. Pin the session time zone so timestamp
        # literals and the replaceWhere condition are not shifted by the
        # cluster / workspace default time zone.
        self.spark.conf.set("spark.sql.session.timeZone", "UTC")
        self.raw_table = raw_table
        self.mapping_table = mapping_table
        self.output_table = output_table
        if read_padding_minutes < 0:
            raise ValueError("read_padding_minutes cannot be negative")
        self.read_padding_minutes = read_padding_minutes

    def run(self, start_time, end_time, calculation):
        """Recompute one calculation within the UTC window."""
        if not isinstance(calculation, str):
            raise TypeError("calculation must be a string")
        if calculation not in self.kpi_registry:
            raise ValueError(f"Unsupported calculation: {calculation}")
        return self._run(start_time, end_time, calculation)

    def run_all(self, start_time, end_time):
        """Recompute all configured calculations within the UTC window."""
        return self._run(start_time, end_time, None)

    def _run(self, start_time, end_time, calculation):
        """Recompute one calculation, or all when calculation is None."""
        start = self._parse_timestamp(start_time)
        end = self._parse_timestamp(end_time)
        if start >= end:
            raise ValueError("start_time must be earlier than end_time")
        calculation_label = (
            calculation if calculation is not None else "all calculations"
        )

        logger.info(
            "Starting KPI run for %s in [%s, %s) using raw table %s and mapping table %s",
            calculation_label,
            start,
            end,
            self.raw_table,
            self.mapping_table,
        )
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

        mapping = mapping.select(
            "plant_id",
            "calculation",
            "specific_measurement_id",
            "specific_measurement_name",
        )
        if calculation is not None:
            mapping = mapping.filter(F.col("calculation") == calculation)
        mapping_rows = mapping.collect()
        if not mapping_rows:
            if calculation is None:
                raise ValueError("Mapping table contains no configured measurements")
            raise ValueError(
                f"Mapping table contains no configured measurements for {calculation}"
            )

        grouped_mappings = {}
        for row in mapping_rows:
            plant_id = row["plant_id"]
            mapping_calculation = row["calculation"]
            measurement_id = row["specific_measurement_id"]
            measurement_column = row["specific_measurement_name"]
            if (
                not plant_id
                or not mapping_calculation
                or not measurement_id
                or not measurement_column
            ):
                raise ValueError(f"Invalid mapping row: {row}")
            if mapping_calculation not in self.kpi_registry:
                raise ValueError(
                    f"Unsupported calculation in mapping table: {mapping_calculation}"
                )
            grouped_mappings.setdefault((plant_id, mapping_calculation), []).append(
                (measurement_column, measurement_id)
            )
        logger.info(
            "Loaded %d mappings across %d plant/calculation groups",
            len(mapping_rows),
            len(grouped_mappings),
        )

        raw = self.spark.table(self.raw_table)
        required_raw_columns = {
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
        logger.info(
            "Reading raw measurements from %s through %s (exclusive)",
            padded_start,
            padded_end,
        )
        raw = raw.filter(
            (F.col("timestamp") >= F.expr(self._sql_timestamp(padded_start)))
            & (F.col("timestamp") < F.expr(self._sql_timestamp(padded_end)))
        )

        outputs = []
        for (plant_id, calculation), measurements in grouped_mappings.items():
            logger.info(
                "Calculating %s for plant %s using %d mapped measurements",
                calculation,
                plant_id,
                len(measurements),
            )
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
            mapped_raw = pro.check_and_deduplicate(mapped_raw)
            kpi = self.kpi_registry[calculation]()
            calculated = kpi.calculate(mapped_raw)
            value_column = kpi.rollup_columns[0]
            missing = {
                "plant_id",
                "timestamp",
                value_column,
                "n_signals_used",
                "source_flag",
            }.difference(calculated.columns)
            if missing:
                raise ValueError(
                    f"{calculation}.calculate() did not produce: "
                    + ", ".join(sorted(missing))
                )

            # calculate() already returns one row per (plant_id, timestamp).
            # The runner only trims the padded read back down to the window.
            result = (
                calculated.filter(
                    (F.col("timestamp") >= F.expr(self._sql_timestamp(start)))
                    & (F.col("timestamp") < F.expr(self._sql_timestamp(end)))
                )
                .withColumn("value", F.col(value_column).cast("double"))
                .withColumn("calculation", F.lit(calculation))
                .select(
                    "plant_id",
                    "timestamp",
                    "calculation",
                    "value",
                    "n_signals_used",
                    "source_flag",
                )
            )
            outputs.append(result)

        output = outputs[0]
        for result in outputs[1:]:
            output = output.unionByName(result)

        self._write(output, start, end, calculation)
        logger.info(
            "Completed %s KPI run for [%s, %s); results written to %s",
            calculation_label,
            start,
            end,
            self.output_table,
        )
        return output

    def _write(self, output, start, end, calculation):
        """Replace rows for this run in [start, end); leave all others alone."""
        replace_condition = (
            f"`timestamp` >= {self._sql_timestamp(start)} "
            f"AND `timestamp` < {self._sql_timestamp(end)}"
        )
        calculation_label = (
            calculation if calculation is not None else "all calculations"
        )
        if calculation is not None:
            escaped_calculation = calculation.replace("'", "''")
            replace_condition += f" AND `calculation` = '{escaped_calculation}'"
        logger.info(
            "Replacing %s rows in %s for [%s, %s)",
            calculation_label,
            self.output_table,
            start,
            end,
        )
        (
            output.write.format("delta")
            .mode("overwrite")
            .option("replaceWhere", replace_condition)
            .saveAsTable(self.output_table)
        )

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