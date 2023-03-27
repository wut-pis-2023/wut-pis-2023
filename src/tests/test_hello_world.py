import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark():
    spark = SparkSession.builder.appName("pytest_hello_world").master("local[*]").getOrCreate()
    yield spark
    spark.stop()


def test_hello_world(spark):
    data = ['Hello,', 'World!']
    rdd = spark.sparkContext.parallelize(data)
    result = rdd.collect()
    assert result == ['Hello,', 'World!']
