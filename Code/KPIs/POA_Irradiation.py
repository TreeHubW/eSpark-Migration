import KPI
import processing as pro
from pyspark.sql import Window
from pyspark.sql import functions as F

class POA_Irradiation(KPI):
    def __init__(self):
        self.name = "POA Irradiation"
        self.description = "Calculates the Plane of Array (POA) Irradiation based on the input data."
        self.dependencies = []
        self.rollup_columns = ["poa_irradiation"]

    def rollup(self, df, grouping_keys):
        return df.groupBy(*grouping_keys).agg(
            F.sum("poa_irradiation").alias("poa_irradiation")
        )

    def calculate(self, df):
        df = pro._ensure_bad_flag(df)
        df = pro.frozen(df, count=10)
        df = pro.bounds(df, min_value=0, max_value=1500)
        df = pro.peer_median(df, range=10)

        timestamp_signal_window = Window.partitionBy("timestamp", "signal_name")
        df = df.withColumn(
            "share_within_peer_median",
            F.avg("within_peer_median_10pct").over(timestamp_signal_window),
        )

        peer_filtered_average = F.avg(
            F.when(
                (F.col("is_frozen") == 0)
                & (F.col("within_bounds") == 1)
                & (F.col("within_peer_median_10pct") == 1),
                F.col("value"),
            )
        ).over(timestamp_signal_window)
        passed_average = F.avg(
            F.when(
                (F.col("is_frozen") == 0) & (F.col("within_bounds") == 1),
                F.col("value"),
            )
        ).over(timestamp_signal_window)
        df = df.withColumn(
            "poa_irradiation",
            F.when(
                F.col("share_within_peer_median") > 0.5,
                peer_filtered_average,
            ).otherwise(passed_average),
        )

        return df

        