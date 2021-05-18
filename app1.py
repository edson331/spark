import sys
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext

spark = SparkSession.builder.getOrCreate()

df = spark.read.options(header='True', inferSchema='True').csv( sys.argv[1] )
df.createOrReplaceTempView("data")
val = spark.sql("select product_id, sum(price) from data group by product_id")
val.rdd.saveAsTextFile( sys.argv[2] )

