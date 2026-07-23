from pyspark.sql.functions import max, min, avg, count, round
import sys

catalog = sys.argv[1]

df = spark.read.table(f"{catalog}.02_silver.silver_citibike_tripdata")

df_summary = (
    df.groupBy("trip_start_date")
    .agg(
        round(max("trip_duration_mins"), 2).alias("max_trip_duration_mins"),
        round(min("trip_duration_mins"), 2).alias("min_trip_duration_mins"),
        round(avg("trip_duration_mins"), 2).alias("avg_trip_duration_mins"),
        count("ride_id").alias("total_trips"),
    )
    .sort(df.trip_start_date.asc())
)

(
    df_summary.write.mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable(f"{catalog}.03_gold.gold_citibike_daily_summary")
)
