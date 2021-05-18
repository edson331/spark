import sys
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext

spark = SparkSession.builder.getOrCreate()

df = spark.read.options(header='True', inferSchema='True').csv( sys.argv[1] )
df.createOrReplaceTempView("data")
val = spark.sql("select brand, count(product_id) from data group by brand")
val.rdd.saveAsTextFile( sys.argv[2] )

