from __future__ import print_function
import sys
from pyspark.sql import SparkSession


def multiply(row, vect):
    if int(row[1]) in vect:
        return [(int(row[0]), float(row[2]) * vect[int(row[1])])]
    return []


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: matrix_vector.py directory_matrix", file=sys.stderr)
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonMatrixVectorSmall") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    vector = {0: 2, 1: -3, 3: 9, 4: 1, 5: 2, 6: 2, 8: 1}

    out = spark.sparkContext.textFile(sys.argv[1]) \
        .map(lambda line: line.strip().split(';')) \
        .flatMap(lambda r: multiply(r, vector)) \
        .reduceByKey(lambda a, b: a + b)

    for i in out.collect():
        print(i)


    # out = []
    # for i in range(1, len(sys.argv)):
    #     out.append(spark.read.csv(sys.argv[i], sep=";")
    #                .rdd
    #                .map(lambda r: (int(r[0]), float(r[2]) * float(vector[int(r[1])])))
    #                )
    #
    # k = 0
    # for i in out:
    #     k += 1
    #     print('Part', k)
    #     for j in i.collect():
    #         print(j)

    # Wersja 2

    # out = spark.sparkContext \
    #     .union([
    #     spark.read.csv(sys.argv[i], sep=";") \
    #         .rdd
    #         .map(lambda r: (int(r[0]), float(r[2]) * float(vector[int(r[1])])))
    #     for i in range(1, len(sys.argv))
    # ]).reduceByKey(lambda a, b: a + b)
    #
    # for i in out.collect():
    #     print(i)
