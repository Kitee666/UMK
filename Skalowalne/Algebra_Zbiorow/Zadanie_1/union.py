from __future__ import print_function
import sys
from pyspark.sql import SparkSession


def Map(r):
    line = r.split()
    if len(line) == 2:
        return [(line[1], line[1])]
    return []


def Reduce(r):
    key, values = r[0], r[1]
    return key


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: union <file>", file=sys.stderr)
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonUnion") \
        .getOrCreate()
    spark.sparkContext.setLogLevel("WARN")

    lines = spark.read.text(sys.argv[1]) \
        .rdd \
        .map(lambda f: f[0])

    union = lines \
        .flatMap(Map) \
        .groupByKey() \
        .map(Reduce)

    # Alternatywnie
    # union = lines \
    #     .flatMap(Map) \
    #     .reduceByKey(lambda a, b: a) \
    #     .map(lambda p: p[0])

    for i in union.collect():
        print(i)
    spark.stop()
