from __future__ import print_function
import sys
from pyspark.sql import SparkSession


def Map(r):
    line = r.split()
    if len(line) == 2:
        return [(line[1], line[0])]
    return []


def Reduce(r):
    key, values = r[0], list(r[1])
    if 'A' in values and 'B' not in values:
        return [key]
    else:
        return []


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: difference <file>", file=sys.stderr)
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonDifference") \
        .getOrCreate()
    spark.sparkContext.setLogLevel("WARN")

    lines = spark.read.text(sys.argv[1]) \
        .rdd \
        .map(lambda f: f[0])

    difference = lines \
        .flatMap(Map) \
        .groupByKey() \
        .flatMap(Reduce)

    for i in difference.collect():
        print(i)
    spark.stop()
