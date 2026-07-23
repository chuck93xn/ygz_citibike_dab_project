from pyspark.sql.functions import unix_timestamp, col


def get_trip_duration_mins(spark, df, start_col, end_col, output_col):
    """
    Calculate the trip duration in minutes based on the start and end timestamps.

    Parameters:
    spark (SparkSession): The Spark session.
    df (DataFrame): The input DataFrame containing the trip data.
    start_col (str): The name of the column containing the start timestamp.
    end_col (str): The name of the column containing the end timestamp.
    output_col (str): The name of the output column to store the trip duration in minutes.

    Returns:
    DataFrame: A new DataFrame with an additional column for trip duration in minutes.
    """
    return df.withColumn(output_col, (unix_timestamp(col(end_col)) - unix_timestamp(col(start_col))) / 60)
