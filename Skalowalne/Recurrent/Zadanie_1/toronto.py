from __future__ import print_function
import sys
from pyspark.sql import SparkSession

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: toronto.py routesFile K", file=sys.stderr)
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonToronto") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    routes = spark.read.csv(sys.argv[1], header=True, sep=",") \
        .rdd \
        .map(lambda it: (it['Source airport'], it['Destination airport'])) \
        .distinct()

    start = spark.sparkContext.parallelize(['YTO', 'YYZ', 'YTZ', 'YHM', 'YKF']) \
        .map(lambda it: (it, None))

    k = int(sys.argv[2])
    for i in range(k):
        print("Obrot %d" % (i + 1))

        next_station = routes \
            .join(start) \
            .map(lambda it: (it[1][0], None))

        start = start \
            .union(next_station) \
            .distinct()

    print("Zebrano %d wyników" % start.count())
