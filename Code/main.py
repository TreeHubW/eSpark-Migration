import logging

from pyspark.sql import SparkSession

from runner import Runner


START_TIME = "2026-08-01T00:00:00Z"
END_TIME = "2026-09-01T00:00:00Z"


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    )
    spark = SparkSession.builder.getOrCreate()
    Runner(spark).run(START_TIME, END_TIME)


if __name__ == "__main__":
    main()
