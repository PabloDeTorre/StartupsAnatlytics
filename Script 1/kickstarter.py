from __future__ import division
from pyspark.sql import SparkSession
from collections import defaultdict
import csv

# Creamos el contexto de Spark
spark = SparkSession.builder.appName("Script").getOrCreate()
sc = spark.sparkContext

# Leemos el archivo, limpamos los caracteres no-ASCII y lo leemos como un csv
file = sc.textFile("./ks-projects-201801.csv")
file = file.map(lambda line: "".join([i if ord(i) < 128 else ' ' for i in line]))
file = file.mapPartitions(lambda x: csv.reader(x))

# Eliminamos la cabecera
header = file.first()
proyects = file.filter(lambda line: line != header)

# Funcion que comprueba si un proyecto se ha completado
def success(x):
	if x == 'successful':
		return 1
	else:
		return 0

# Calculamos el numero total de proyectos para cada categoria
pTotal = proyects.map(lambda p: (str(p[3]),1))
pTotal = pTotal.reduceByKey(lambda x,y: x+y)

# Calculamos el numero de proyectos que se completan para cada categoria
pSuccessful = proyects.map(lambda p: (str(p[3]),int(success(p[9]))))
pSuccessful = pSuccessful.reduceByKey(lambda x,y: x+y)

# Calculamos el total de ganancias por categoria de los proyectos completados
pEarnings = proyects.filter(lambda p: p[9] == 'successful')
pEarnings = pEarnings.map(lambda p: (str(p[3]),float(p[13])))
pEarnings = pEarnings.reduceByKey(lambda x,y: x+y)

# Generamos el resultado con el formato ((%exito, avg(ganancias), nombre)
pResult = pEarnings.join(pTotal).join(pSuccessful)
pResult = pResult.map(lambda p: ((float((p[1][1]/p[1][0][1])*100),float(p[1][0][0]/p[1][1])),p[0]))

# Ordenamos por %exito y generamos la salida
pPercentage = pResult.sortByKey(False)
pPercentage.saveAsTextFile("./Promedio_Exito")

# Ordenamos po avg(ganancias) y generamos otra salida
pAvg = pResult.map(lambda p: ((p[0][1], p[0][0]), p[1]))
pAvg = pAvg.sortByKey(False)
pAvg.saveAsTextFile("./Media_Ganancias")

sc.stop()
