from pyspark.sql.functions import to_date, col


def timestamp_to_date_col(spark, df, timestamp_col, output_col):
    """
    Convert a timestamp column to a date column.

    Parameters:
    spark (SparkSession): The Spark session.
    df (DataFrame): The input DataFrame containing the timestamp data.
    timestamp_col (str): The name of the column containing the timestamp.
    output_col (str): The name of the output column to store the date.

    Returns:
    DataFrame: A new DataFrame with an additional column for the date.
    """
    return df.withColumn(output_col, to_date(col(timestamp_col)))
