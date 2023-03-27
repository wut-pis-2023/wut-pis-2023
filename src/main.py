from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("HelloWorld").getOrCreate()

    data = ['Hello,', 'World!']
    rdd = spark.sparkContext.parallelize(data)

    print("RDD zawartość:")
    for element in rdd.collect():
        print(element)

    spark.stop()
