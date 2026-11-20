import logging

from pyspark.sql import SparkSession


logger = logging.getLogger(__name__)

def create_tables(spark):
    """Create tables and reseed mappings for a fresh test run."""
    logger.info("Creating Mapping_Table if it does not exist")
    spark.sql(
        """
        CREATE TABLE IF NOT EXISTS Mapping_Table (
            plant_id STRING,
            plant_name STRING,
            calculation STRING,
            specific_measurement_id STRING,
            specific_measurement_name STRING,
            timestamp_valid TIMESTAMP,
            source_system STRING
        )
        USING DELTA
        """
    )
    logger.warning("Clearing Mapping_Table before inserting test mappings")
    spark.sql("TRUNCATE TABLE Mapping_Table")
    spark.sql("INSERT INTO Mapping_Table VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'UNIVERS/f0be4242-5738-4df8-aa93-ab2a452a8545', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql("INSERT INTO Mapping_Table VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'UNIVERS/ee1c4784-969b-4b64-84b6-c9eb0b969abb', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql("INSERT INTO Mapping_Table VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'UNIVERS/d3bae6c9-eb2d-4989-94a9-29c08d231a41', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql("INSERT INTO Mapping_Table VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'UNIVERS/72128904-e225-48c0-b332-4838dedeb7ef', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql("INSERT INTO Mapping_Table VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'UNIVERS/73403b6e-72e6-4556-8fb1-be7b0e6d8248', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql("INSERT INTO Mapping_Table VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'UNIVERS/824f5816-86e0-4ed4-8812-c191f29b3901', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql("INSERT INTO Mapping_Table VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'UNIVERS/098dc82a-4744-4bbc-b090-529ba267d518', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql("INSERT INTO Mapping_Table VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'UNIVERS/35c7e6ee-b78a-476d-9b91-59356e025744', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")

    logger.info("Inserted 8 test mappings into Mapping_Table")
    logger.warning("Replacing POA_Irradiation; existing test output will be dropped")
    spark.sql(
        """
        CREATE OR REPLACE TABLE POA_Irradiation (
            plant_id STRING,
            timestamp TIMESTAMP,
            calculation STRING,
            value DOUBLE,
            n_signals_used INT,
            source_flag STRING
        )
        USING DELTA
        """
    )
    logger.info("Created POA_Irradiation with the current output schema")
        


if __name__ == "__main__":
    create_tables(SparkSession.builder.getOrCreate())
