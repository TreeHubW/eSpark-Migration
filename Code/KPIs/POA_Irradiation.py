import logging

from .KPI import KPI
import processing as pro
from pyspark.sql import functions as F


logger = logging.getLogger(__name__)


class POA_Irradiation(KPI):
    # Share of evaluated sensors that must be within the peer band for the
    # peer-filtered average to be used (strictly greater than).
    PEER_SHARE_THRESHOLD = 0.5

    @property
    def name(self):
        return "POA Irradiation"

    @property
    def description(self):
        return "Calculates Plane of Array irradiation from cleaned input data."

    @property
    def dependencies(self):
        return []

    @property
    def rollup_columns(self):
        return ["poa_irradiation"]

    def rollup(self, df, grouping_keys):
        return df.groupBy(*grouping_keys).agg(
            F.sum("value").alias("poa_irradiation")
        )

    def calculate(self, df):
        """
        input:  one row per (plant_id, key, timestamp), where key is one sensor
        output: one row per (plant_id, timestamp) with
                    poa_irradiation  value, null if no sensor was usable
                    n_signals_used   how many sensors went into the value
                    source_flag      peer_filtered | passed_avg_fallback |
                                     no_valid_signal

        Partitioning of each stage (this is what has to stay consistent):
            frozen        per sensor            (plant_id, key) ordered by time
            bounds        per reading           no partition
            peer_median   per plant + time span (plant_id, [t, t+10min)), excluding own key
            final average per plant + instant   (plant_id, timestamp), ALL sensors together
        The first three produce per-sensor flags. Only the last one crosses
        sensors, so it is the only stage that may collapse the key column.
        """
        df = pro._ensure_bad_flag(df)
        logger.debug("Building POA frozen-value, bounds, and peer-check stages")
        df = pro.frozen(df, count=10)
        df = pro.bounds(df, min_value=0, max_value=1500)
        df = pro.peer_median(df, range=10)

        passed_earlier_checks = (F.col("is_frozen") == 0) & (F.col("within_bounds") == 1)
        passed_peer_check = passed_earlier_checks & (F.col("within_peer_median_10pct") == 1)

        logger.debug(
            "Building plant/timestamp POA aggregation with peer-share threshold > %s",
            self.PEER_SHARE_THRESHOLD,
        )
        return (
            df.groupBy("plant_id", "timestamp")
            .agg(
                # Average of sensors that passed every check.
                F.avg(F.when(passed_peer_check, F.col("value"))).alias("_peer_filtered_avg"),
                # Average of sensors that passed everything except possibly the peer band.
                F.avg(F.when(passed_earlier_checks, F.col("value"))).alias("_passed_avg"),
                # Share within the band among sensors that were actually evaluated
                # (flagged / no-peer rows are null and ignored by avg).
                F.avg("within_peer_median_10pct").alias("_share_within_peer"),
                F.count(F.when(passed_peer_check, 1)).alias("_n_peer_filtered"),
                F.count(F.when(passed_earlier_checks, 1)).alias("_n_passed"),
            )
            .withColumn(
                "_use_peer_filtered",
                F.col("_share_within_peer") > F.lit(self.PEER_SHARE_THRESHOLD),
            )
            .withColumn(
                "poa_irradiation",
                F.when(F.col("_use_peer_filtered"), F.col("_peer_filtered_avg"))
                .otherwise(F.col("_passed_avg")),
            )
            .withColumn(
                "n_signals_used",
                F.when(F.col("_use_peer_filtered"), F.col("_n_peer_filtered"))
                .otherwise(F.col("_n_passed"))
                .cast("int"),
            )
            .withColumn(
                "source_flag",
                F.when(F.col("_use_peer_filtered"), F.lit("peer_filtered"))
                .when(F.col("_n_passed") > 0, F.lit("passed_avg_fallback"))
                .otherwise(F.lit("no_valid_signal")),
            )
            .select("plant_id", "timestamp", "poa_irradiation", "n_signals_used", "source_flag")
        )
