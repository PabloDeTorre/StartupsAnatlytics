import sys
from pyspark import SparkContext
from operator import add
from pyspark.sql import functions
import math
from pyspark.sql import SQLContext



input_file = "ks-projects-201801.csv"
sc = SparkContext('local', 'Script')
sqlContext = SQLContext(sc)

df = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load(input_file)
df.printSchema()
lines = df.select('category','backers','pledged','goal').filter("pledged is not NULL").filter("backers is not NULL").filter(functions.col('pledged') > functions.col('goal')).groupBy('category').agg(functions.avg('pledged'),functions.avg('backers'),(functions.mean('pledged')/functions.mean('backers'))).withColumnRenamed("(avg(pledged) / avg(backers))", "MediaDonadoPorDonador").filter("MediaDonadoPorDonador is not NULL").withColumnRenamed("category", "Categorias Con Exitos").withColumnRenamed("avg(pledged)", "MediaDonado").withColumnRenamed("avg(backers)", "MediaDonadores").orderBy('MediaDonadoPorDonador',ascending=False)
lines.show()
lines.printSchema()
lines.coalesce(1).write.csv("output")
