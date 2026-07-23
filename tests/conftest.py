import os
import sys
import pytest

os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
os.environ.setdefault("PYSPARK_DRIVER_PYTHON", sys.executable)

sys.path.append(os.getcwd())


@pytest.fixture()
def spark():
    try:
        from databricks.connect import DatabricksSession

        spark = DatabricksSession.builder.getOrCreate()
    except ImportError:
        try:
            from pyspark.sql import SparkSession

            spark = SparkSession.builder.getOrCreate()
        except ImportError:
            raise ImportError("Neither Databricks session or Spark session")

    # return spark
    yield spark
    spark.stop()
