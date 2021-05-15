from __future__ import print_function
import sys
from pyspark.sql import SparkSession


def myJoin(row):
    rowA = list(filter(lambda r: r[0] == 'A', row))
    colB = list(filter(lambda r: r[0] == 'B', row))
    return [((r[1], c[1]), r[2] * c[2]) for r in rowA for c in colB]


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: matrix_matrix.py directory_matrix_A directory_matrix_B", file=sys.stderr)
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonMatrixMatrix") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    matrixA = spark.sparkContext.textFile(sys.argv[1]) \
        .map(lambda line: line.strip().split(';')) \
        .map(lambda r: (int(r[1]), ('A', int(r[0]), float(r[2]))))

    matrixB = spark.sparkContext.textFile(sys.argv[2]) \
        .map(lambda line: line.strip().split(';')) \
        .map(lambda r: (int(r[0]), ('B', int(r[1]), float(r[2]))))

    matrixC = matrixA.union(matrixB) \
        .groupByKey() \
        .flatMap(lambda p: myJoin(p[1])) \
        .map(lambda it: it) \
        .reduceByKey(lambda a, b: a + b)

    for i in matrixC.collect():
        print(i)

    # out = []
    # k = 0
    # for i in range(1, len(sys.argv), 2):
    #     out.append(
    #         spark.read.csv(sys.argv[i], sep=";") \
    #             .rdd \
    #             .map(lambda r: (int(r[1]), (int(r[0]), float(r[2])))) \
    #             .join(spark.read.csv(sys.argv[i + 1], sep=";") \
    #                   .rdd \
    #                   .map(lambda r: (int(r[0]), (int(r[1]), float(r[2]))))
    #                   ) \
    #             .map(lambda r: ((r[1][0][0], r[1][1][0]), r[1][0][1] * r[1][1][1]))
    #     )
    #
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
    #         .rdd \
    #         .map(lambda r: (int(r[1]), (int(r[0]), float(r[2])))) \
    #         .join(spark.read.csv(sys.argv[i + 1], sep=";") \
    #               .rdd \
    #               .map(lambda r: (int(r[0]), (int(r[1]), float(r[2]))))
    #               ) \
    #         .map(lambda r: ((r[1][0][0], r[1][1][0]), r[1][0][1] * r[1][1][1]))
    #     for i in range(1, len(sys.argv), 2)
    # ]).reduceByKey(lambda a, b: a + b)
    #
    # for i in out.collect():
    #     print(i)
