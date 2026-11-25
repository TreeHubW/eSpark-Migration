import logging

from pyspark.sql import SparkSession


logger = logging.getLogger(__name__)

# Unity Catalog location (catalog.schema) for all project tables.
SCHEMA = "espark_consumer_group.us_performance"
MAPPING_TABLE = f"{SCHEMA}.Mapping_Table"
OUTPUT_TABLE = f"{SCHEMA}.POA_Irradiation"

def create_tables(spark):
    """Create tables and reseed mappings for a fresh test run."""
    logger.info("Creating Mapping_Table if it does not exist")
    spark.sql(
        f"""
        CREATE TABLE IF NOT EXISTS {MAPPING_TABLE} (
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
    spark.sql(f"TRUNCATE TABLE {MAPPING_TABLE}")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'UNIVERS/f0be4242-5738-4df8-aa93-ab2a452a8545', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'UNIVERS/ee1c4784-969b-4b64-84b6-c9eb0b969abb', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'UNIVERS/d3bae6c9-eb2d-4989-94a9-29c08d231a41', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'UNIVERS/72128904-e225-48c0-b332-4838dedeb7ef', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'UNIVERS/73403b6e-72e6-4556-8fb1-be7b0e6d8248', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'UNIVERS/824f5816-86e0-4ed4-8812-c191f29b3901', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'UNIVERS/098dc82a-4744-4bbc-b090-529ba267d518', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'UNIVERS/35c7e6ee-b78a-476d-9b91-59356e025744', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")

    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-154.10-Pyranometer - POA 02/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-053.04-Pyranometer - POA 01/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-134.09-Pyranometer - POA 01/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-053.04-Pyranometer - POA 02/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-085.07-Pyranometer - POA 01/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-111.08-Pyranometer - POA 01/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-002.01-Pyranometer - POA 02/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-067.05-Pyranometer - POA 02/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-085.07-Pyranometer - POA 02/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-134.09-Pyranometer - POA 02/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-067.05-Pyranometer - POA 01/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-031.03-Pyranometer - POA 02/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-081.06-Pyranometer - POA 01/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-179.11-Pyranometer - POA 01/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-081.06-Pyranometer - POA 02/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-028.02-Pyranometer - POA 01/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-002.01-Pyranometer - POA 01/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-031.03-Pyranometer - POA 01/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-179.11-Pyranometer - POA 02/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-028.02-Pyranometer - POA 02/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-111.08-Pyranometer - POA 02/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql(f"INSERT INTO {MAPPING_TABLE} VALUES ('5645a80249489ddd8088e990660364139836f8aa4a9f49c6ab66bd8161e0760a', 'DanishT3', 'POA_Irradiation', 'powerfactors_5074.01.002_MET-154.10-Pyranometer - POA 01/IRRADIANCE_POA', 'signal_id', '2026-11-19 00:00:00', 'UNIVERS')")

    logger.info("Inserted 29 test mappings into Mapping_Table")
    logger.warning("Replacing POA_Irradiation; existing test output will be dropped")
    spark.sql(
        f"""
        CREATE OR REPLACE TABLE {OUTPUT_TABLE} (
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
