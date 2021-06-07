from __future__ import print_function
import sys
from pyspark.sql import SparkSession

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: cities.py routesFile K", file=sys.stderr)
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonCities") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    routes = spark.read.csv(sys.argv[1], header=True, sep=",") \
        .rdd \
        .map(lambda it: (it['Source airport'], it['Destination airport'])) \
        .distinct()

    # start = spark.sparkContext.parallelize(['BZG', 'WAW', 'WMI']) \
    #     .map(lambda it: (it, 0))
    start = spark.sparkContext.parallelize(['BZG']) \
            .map(lambda it: (it, 0))
    toVisit = start.map(lambda it: (it[0], 0))

    k = int(sys.argv[2])
    for i in range(k):
        print("Obrot %d" % (i + 1))

        next_station = routes \
            .join(toVisit) \
            .map(lambda it: (it[1][0], it[1][1] + 1))

        toVisit = next_station.subtractByKey(start)

        start = start \
            .union(next_station) \
            .reduceByKey(lambda a, b: min(a, b))

    print("Zebrano %d wyników" % start.count())
    for i in start.collect():
        print(i)
