from __future__ import print_function
import sys
from pyspark.sql import SparkSession


def multiply(row, vect):
    if int(row[1]) in vect:
        return [(int(row[0]), float(row[2]) * vect[int(row[1])])]
    return []


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: pagerank_taxation.py directory_matrix connection_number", file=sys.stderr)
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonPagerankTaxation") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    matrix = spark.read.csv(sys.argv[1], header=False, sep=";").rdd

    vector = dict((i, 1.0 / float(sys.argv[2])) for i in range(int(sys.argv[2])))

    dist = int(sys.argv[2])

    beta = 0.8

    print(vector)
    for _ in range(50):
        vector = matrix \
            .flatMap(lambda r: multiply(r, vector)) \
            .reduceByKey(lambda a, b: a + b) \
            .map(lambda v: (v[0], beta * v[1] + (1 - beta) * 1 / dist)) \
            .collectAsMap()

        print(vector)

    spark.stop()
