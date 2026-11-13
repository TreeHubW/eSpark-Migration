from pyspark.sql import SparkSession


TABLE_NAME = "`Mapping Table`"


def create_tables(spark):
    """Create the mapping table if needed, then clear it for a fresh test run."""
    spark.sql(
        f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            plant_id STRING,
            calculation STRING,
            signal_id STRING,
            source_system STRING,
            grouping STRING
        )
        USING DELTA
        """
    )
    spark.sql(f"TRUNCATE TABLE {TABLE_NAME}")
    print("Mapping Table is ready and empty.")


if __name__ == "__main__":
    create_tables(SparkSession.builder.getOrCreate())