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
        .map(lambda it: (it, 0))
    toVisit = start.map(lambda it: (it[0], 0))

    i = 0
    counter = 3
    while counter > 0:
        print("Obrot %d" % (i + 1))
        print("Odlot z %d" % counter)
        next_station = routes \
            .join(toVisit) \
            .map(lambda it: (it[1][0], it[1][1] + 1))

        toVisit = next_station.subtractByKey(start)
        counter = toVisit.count()
        i += 1

        start = start \
            .union(next_station) \
            .reduceByKey(lambda a, b: min(a, b))

    print("Zebrano %d wyników" % start.count())
