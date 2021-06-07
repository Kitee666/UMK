from __future__ import print_function
import sys
from pyspark.sql import SparkSession

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: no_limit.py routesFile ", file=sys.stderr)
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonNoLimit") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    routes = spark.read.csv(sys.argv[1], header=True, sep=",") \
        .rdd \
        .map(lambda it: (it['Source airport'], it['Destination airport'])) \
        .distinct()

    start = spark.sparkContext.parallelize(['BZG', 'WAW', 'WMI']) \
        .map(lambda it: (it, None))

    counter = 0
    oldLen = 0
    newLen = start.count()
    while oldLen != newLen:
        print("Obrot %d" % (counter + 1))

        counter += 1
        oldLen = newLen
        next_station = routes \
            .join(start) \
            .map(lambda it: (it[1][0], None))

        start = start \
            .union(next_station) \
            .distinct()

        newLen = start.count()
        print("Aktualnie zebrano %d danych" % newLen)

    print("Zebrano %d wyników" % start.count())

    spark.stop()
