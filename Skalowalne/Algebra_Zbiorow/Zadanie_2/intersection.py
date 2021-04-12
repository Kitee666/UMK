from __future__ import print_function
import sys
from pyspark.sql import SparkSession


def Map(r):
    line = r.split()
    if len(line) == 2:
        return [(line[1], line[1])]
    return []


def Reduce(r):
    key, values = r[0], list(r[1])
    if len(values) == 2 and values.count(key) == 2:
        return [key]
    else:
        return []


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: intersection <file>", file=sys.stderr)
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonIntersection") \
        .getOrCreate()
    spark.sparkContext.setLogLevel("WARN")

    lines = spark.read.text(sys.argv[1]) \
        .rdd \
        .map(lambda f: f[0])

    intersection = lines \
        .flatMap(Map) \
        .groupByKey() \
        .flatMap(Reduce)

    for i in intersection.collect():
        print(i)
    spark.stop()
