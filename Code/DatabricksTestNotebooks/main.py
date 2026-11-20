import logging
import sys
import time
from datetime import datetime

import importlib
from pyspark.sql import functions as F
import processing
import KPIs.POA_Irradiation as poa_module
import runner as runner_module

CODE_PATH = "/Workspace/Users/fady.seha@totalenergies.com/eSpark-Migration/Code"
MAPPING_TABLE = "espark_consumer_group.us_performance.Mapping_Table"
OUTPUT_TABLE = "espark_consumer_group.us_performance.POA_Irradiation"
START_TS = "2026-08-01T00:00:00Z"
END_TS = "2026-09-01T00:00:00Z"

_t0 = time.time()


def log(msg):
    """Print a timestamped checkpoint with elapsed seconds since start."""
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now} | +{time.time() - _t0:7.1f}s] {msg}", flush=True)


# Databricks pre-installs root log handlers; force=True replaces them so the
# logger.info(...) messages from runner/processing show up in the output.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    force=True,
)

log("START main.py")
sys.path.append(CODE_PATH)

# Reload so edits to processing.py / KPIs / runner.py are picked up without
# restarting Python. Order matters: dependencies first, runner last.
importlib.reload(processing)
importlib.reload(poa_module)
importlib.reload(runner_module)
Runner = runner_module.Runner

log(f"Mapping table : {MAPPING_TABLE}")
log(f"Output table  : {OUTPUT_TABLE}")
log(f"Window        : {START_TS} -> {END_TS}")

runner = Runner(
    spark,
    mapping_table=MAPPING_TABLE,
    output_table=OUTPUT_TABLE,
)
log("Runner initialised, starting run_all()")

_t_run = time.time()
runner.run_all(START_TS, END_TS)
log(f"run_all() finished in {time.time() - _t_run:.1f}s")

# Read back what was written. Using the DataFrame returned by run() would
# recompute the whole pipeline again for every action below.
result = spark.table(OUTPUT_TABLE).filter(
    (F.col("timestamp") >= F.to_timestamp(F.lit(START_TS)))
    & (F.col("timestamp") < F.to_timestamp(F.lit(END_TS)))
)
log(f"Result columns: {result.columns}")
row_count = result.count()
log(f"Result row count: {row_count:,}")
if row_count == 0:
    log("WARNING: result is empty - check the time window and mapping table")

log("Summary per plant_id / calculation:")
result.groupBy("plant_id", "calculation").agg(
    F.count("*").alias("rows"),
    F.min("timestamp").alias("first_timestamp"),
    F.max("timestamp").alias("last_timestamp"),
    F.avg("n_signals_used").alias("avg_signals_used"),
    F.count(F.when(F.col("source_flag") == "peer_filtered", 1)).alias("peer_filtered"),
    F.count(F.when(F.col("source_flag") == "passed_avg_fallback", 1)).alias("avg_fallback"),
    F.count(F.when(F.col("source_flag") == "no_valid_signal", 1)).alias("no_valid_signal"),
).orderBy("plant_id", "calculation").show(truncate=False)

log("DONE main.py")