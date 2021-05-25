from __future__ import print_function
import sys
from pyspark.sql import SparkSession


def multiply(row, vect):
    if int(row[1]) in vect:
        return [(int(row[0]), float(row[2]) * vect[int(row[1])])]
    return []


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: pagerank_random_walk.py directory_matrix", file=sys.stderr)
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonPagerankRandomWalk") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    # wczytac raz, do rdd i korzystac z macierzy
    #Do 1,2,4
    vector = {0: 0.25, 1: 0.25, 2: 0.25, 3: 0.25}
    #Do 3
    #vector = {0: 0.2, 1: 0.2, 2: 0.2, 3: 0.2, 4: 0.2}
    #Do 5
    #vector = {0: 0.33333333, 1: 0.33333333, 2: 0.33333333}
    for _ in range(50):
        vector = spark.sparkContext.textFile(sys.argv[1]) \
            .map(lambda line: line.strip().split(';')) \
            .flatMap(lambda r: multiply(r, vector)) \
            .reduceByKey(lambda a, b: a + b) \
            .collectAsMap()

        print(vector)

    spark.stop()
