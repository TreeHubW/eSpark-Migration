from pyspark.sql import SparkSession

def create_tables(spark):
    """Create the mapping table if needed, then clear it for a fresh test run."""
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
    spark.sql("INSERT INTO Mapping_Table VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'GG37FN7NBWXCFXFQ2MC3P3TLBSZ3O66YG7Q4GZ3X2SL3HMX6FYMQ', 'equipment_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql("INSERT INTO Mapping_Table VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'CGJASOC2JCLCNY25HGL5ZH4NZX7I4X67YTP7RJRRMVIO6V7G3ZXQ', 'equipment_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql("INSERT INTO Mapping_Table VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'R76EFMN7FEIIHPEM2MXRZF7SQPPG2RQWMPLA2QSO4UR7UQET3DLA', 'equipment_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql("INSERT INTO Mapping_Table VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'ONDR2CHJBPOYQO4WBRRMKUVGGHXEDN4RQYAQCW2CHYZ555JH5UXA', 'equipment_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql("INSERT INTO Mapping_Table VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'CGJASOC2JCLCNY25HGL5ZH4NZX7I4X67YTP7RJRRMVIO6V7G3ZXQ', 'equipment_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql("INSERT INTO Mapping_Table VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'GG37FN7NBWXCFXFQ2MC3P3TLBSZ3O66YG7Q4GZ3X2SL3HMX6FYMQ', 'equipment_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql("INSERT INTO Mapping_Table VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'R76EFMN7FEIIHPEM2MXRZF7SQPPG2RQWMPLA2QSO4UR7UQET3DLA', 'equipment_id', '2026-11-19 00:00:00', 'UNIVERS')")
    spark.sql("INSERT INTO Mapping_Table VALUES ('4GAFWQTFXOHW5R5IWTLX72T7IUO2JPWYVE3O26SUX3EUA7RINV6A', 'Hill 1', 'POA_Irradiation', 'ONDR2CHJBPOYQO4WBRRMKUVGGHXEDN4RQYAQCW2CHYZ555JH5UXA', 'equipment_id', '2026-11-19 00:00:00', 'UNIVERS')")

    spark.sql(
        """
        CREATE TABLE IF NOT EXISTS POA_Irradiation (
            plant_id STRING,
            timestamp TIMESTAMP,
            calculation STRING,
            value DOUBLE,
            bad_flag INT,
            key STRING
        )
        USING DELTA
        """
    )
        


if __name__ == "__main__":
    create_tables(SparkSession.builder.getOrCreate())