from __future__ import print_function
import sys
from pyspark.sql import SparkSession


def multiply(row, vect):
    if int(row[1]) in vect:
        return [(int(row[0]), float(row[2]) * vect[int(row[1])])]
    return []


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: pagerank_taxation.py directory_matrix", file=sys.stderr)
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonPagerankTaxation") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    #Do 1,2,4
    #vector = {0: 0.25, 1: 0.25, 2: 0.25, 3: 0.25}
    #Do 3
    #vector = {0: 0.2, 1: 0.2, 2: 0.2, 3: 0.2, 4: 0.2}
    #Do 5
    vector = {0: 0.33333333, 1: 0.33333333, 2: 0.33333333}
    dist = len(vector)
    beta = 0.8

    for _ in range(50):
        vector = spark.sparkContext.textFile(sys.argv[1]) \
            .map(lambda line: line.strip().split(';')) \
            .flatMap(lambda r: multiply(r, vector)) \
            .reduceByKey(lambda a, b: a + b) \
            .map(lambda v: (v[0], beta * v[1] + (1 - beta) * 1 / dist)) \
            .collectAsMap()

        print(vector)
        dist = len(vector)

    spark.stop()
