# StartupsAnatlytics

Nuestro proyecto se compone de tres scripts, dos de ellos programados en Python y uno en Scala. En todos utilizamos el algoritmo de map-reduce sobre Spark. Para el correcto funcionamiento de ellos necesitaremos tener descargado el fichero csv que contiene los datos de los proyectos, descargable en este [enlace](https://www.kaggle.com/kemical/kickstarter-projects) (también se encuentra en el repositorio).

## Script 1 - Éxito de proyectos
El primer script tiene el objetivo de encontrar cuáles son los tipos de proyectos que más funcionan. Para ello, limpia el csv, obtiene todos los proyectos que han llegado a completarse al 100%, calcula sus beneficios, y los agrupa por categoría.Para ejecutar el script basta con ejecutar en nuestra máquina virtual:
```
spark-submit kickstarter1.py
```
El script generará dos ficheros de salida. El primero, PromedioExito, muestra las categorías ordenadas por porcentaje de éxito, mientras que el segundo, Media_Ganancias, muestra cuáles las categorías ordenadas por mayor número de ganancias. Ambos ficheros se muestran en el formato:
```
PorcentajeÉxito,MediaGanancias,Categoría
```
## Script 2 - Países más financiados
El segundo script se encuentra desarrollado en Scala. Este script muestra cuáles son los países que más donaciones reciben y en qué tipo de categoría. Para ello, filtramos los proyectos los proyectos que han recaudado más de 1 millón de dólares y mostramos en un fichero de salida el país, el tipo de proyecto, la cantidad pedida y la cantidad obtenida de cada proyecto. Para ejecutar el script es necesario disponer de la herramienta IntelliJ. El script generará una salida que muestre:
```
País,Categoría,CantidadObjetivo,CantidadObtenida
```
## Script 3 - Media de donaciones
El tercer y último script de nuestro proyecto está desarrollado en Python, y utiliza la librería de Spark SQL. Este Script nos muestra la media de donantes que tiene cada subcategoría, y la media de donación por donante (ordenado de mayor a menor). Para ejecutar el script hay que escribir en la terminal de nuestra máquina virtual el comando:
```
spark-submit kickstarter3.py
```
Generará una salida que muestre
```
Subcategoría,mediaDonaciones,mediaDonacionPorDonante
```
