import logging

from pyspark.sql import Window
from pyspark.sql import functions as F


logger = logging.getLogger(__name__)


def _ensure_bad_flag(df):
    if "bad_flag" not in df.columns:
        return df.withColumn("bad_flag", F.lit(0))
    return df


def _accumulate_bad_flag(df, failed):
    df = _ensure_bad_flag(df)
    return df.withColumn(
        "bad_flag",
        F.when(
            (F.col("bad_flag") == 1) | F.coalesce(failed, F.lit(False)),
            F.lit(1),
        ).otherwise(F.lit(0)),
    )


def check_and_deduplicate(df):
    """Return one averaged row per plant/key/timestamp and warn about duplicates."""
    grain = ["plant_id", "key", "timestamp"]
    duplicate_groups = df.groupBy(*grain).count().filter(F.col("count") > 1)
    stats = duplicate_groups.agg(
        F.count("*").alias("duplicate_groups"),
        F.coalesce(F.sum(F.col("count") - 1), F.lit(0)).alias("duplicate_rows"),
    ).first()

    if stats["duplicate_groups"]:
        logger.warning(
            "Found %s duplicate plant/key/timestamp groups (%s extra rows); "
            "collapsing each group by averaging value.",
            stats["duplicate_groups"],
            stats["duplicate_rows"],
        )
    else:
        logger.info("No duplicate plant/key/timestamp groups found")

    return df.groupBy(*grain).agg(F.avg("value").alias("value"))


def frozen(df, count=10):
    """
    Flag all but the first reading in a run longer than ``count``.

    :param df: Spark DataFrame with plant_id, key, timestamp, and value
    :param count: Minimum run length required to flag the run
    :return: Spark DataFrame with is_frozen and accumulated bad_flag columns
    """
    logger.debug("Applying frozen-value check with minimum run length %d", count)
    ordered_window = Window.partitionBy("plant_id", "key").orderBy("timestamp")
    running_window = ordered_window.rowsBetween(
        Window.unboundedPreceding, Window.currentRow
    )

    df = df.withColumn(
        "_is_new_run",
        F.when(
            F.lag("value").over(ordered_window).eqNullSafe(F.col("value")),
            F.lit(0),
        ).otherwise(F.lit(1)),
    )
    df = df.withColumn("_frozen_run_id", F.sum("_is_new_run").over(running_window))

    run_window = Window.partitionBy(
        "plant_id", "key", "_frozen_run_id"
    ).orderBy("timestamp")
    df = df.withColumn("_run_position", F.row_number().over(run_window))
    run_length_window = run_window.rowsBetween(
        Window.unboundedPreceding, Window.unboundedFollowing
    )
    df = df.withColumn("_run_length", F.count(F.lit(1)).over(run_length_window))
    df = df.withColumn(
        "is_frozen",
        F.when(
            (F.col("_run_length") > count) & (F.col("_run_position") > 1),
            F.lit(1),
        ).otherwise(F.lit(0)),
    )

    df = df.drop("_is_new_run", "_frozen_run_id", "_run_position", "_run_length")
    return _accumulate_bad_flag(df, F.col("is_frozen") == 1)


def bounds(df, min_value=0, max_value=1500):
    """Flag values outside the inclusive bounds and accumulate bad_flag."""
    logger.debug(
        "Applying value bounds check with inclusive range [%s, %s]",
        min_value,
        max_value,
    )
    df = df.withColumn(
        "within_bounds",
        F.when(F.col("value").between(min_value, max_value), F.lit(1)).otherwise(
            F.lit(0)
        ),
    )
    return _accumulate_bad_flag(df, F.col("within_bounds") == 0)


def peer_median(df, range):
    """
    Compare unflagged readings with the median from other mapped keys at the
    same plant in the next ``range`` minutes.

    Partitioning: the comparison group is (plant_id, [t, t + range)) minus the
    reading's own key. Only readings that survived earlier checks (bad_flag == 0)
    take part, on both sides. Rows already flagged get a null result, so they are
    neither judged here nor counted as a peer-check pass or fail.
    """
    logger.debug("Building peer-median comparison over the next %d minutes", range)
    df = _ensure_bad_flag(df)
    unflagged = df.filter(F.col("bad_flag") == 0)
    base = unflagged.alias("base")
    other = unflagged.alias("other")
    peer_window = base.join(
        other,
        (F.col("base.plant_id") == F.col("other.plant_id"))
        & (F.col("base.key") != F.col("other.key"))
        & (F.col("other.timestamp") >= F.col("base.timestamp"))
        & (
            F.col("other.timestamp")
            < F.col("base.timestamp") + F.expr(f"INTERVAL {range} MINUTES")
        ),
        "inner",
    )
    peers = peer_window.groupBy(
        F.col("base.plant_id").alias("plant_id"),
        F.col("base.key").alias("key"),
        F.col("base.timestamp").alias("timestamp"),
    ).agg(
        F.expr("median(other.value)").alias("peer_median_next_10min"),
        F.count(F.col("other.value")).alias("peer_reading_count"),
        F.countDistinct(F.col("other.key")).alias("peer_measurement_count"),
    )

    source = df.alias("source")
    peer = peers.alias("peer")
    df = source.join(
        peer,
        (F.col("source.plant_id") == F.col("peer.plant_id"))
        & (F.col("source.key") == F.col("peer.key"))
        & (F.col("source.timestamp") == F.col("peer.timestamp")),
        "left",
    ).select(
        "source.*",
        F.col("peer.peer_median_next_10min"),
        F.col("peer.peer_reading_count"),
        F.col("peer.peer_measurement_count"),
    )
    df = df.withColumn(
        "within_peer_median_10pct",
        F.when(
            F.col("peer_median_next_10min").isNull(),
            F.lit(None).cast("int"),
        )
        .when(
            F.abs(F.col("value") - F.col("peer_median_next_10min"))
            <= F.lit(0.10) * F.abs(F.col("peer_median_next_10min")),
            F.lit(1),
        )
        .otherwise(F.lit(0)),
    )
    return _accumulate_bad_flag(
        df,
        F.col("within_peer_median_10pct") == 0,
    )