from __future__ import print_function
import sys
from pyspark.sql import SparkSession


def mapper(r, cluster_size):
    out = []
    row = int(r[0])
    val = float(r[1])
    for edge in range(2, len(r)):
        if r[edge] is not None:
            out.append((int(row // cluster_size), (int(r[edge]), row, 1.0 / val)))
    return out


# def mapper(r):
#     out = []
#     key = int(r[0])
#     val = float(r[1])
#     for edge in range(2, len(r)):
#         if r[edge] is not None:
#             out.append((key, (int(r[edge]), 1.0 / val)))
#     return out


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: pagerank_corrected.py directory_matrix confident vector_files block_size",
              file=sys.stderr)
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonPagerankCorrected") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    cluster_size = int(sys.argv[4])

    matrix = spark.read.csv(sys.argv[1], header=False, sep=";") \
        .rdd \
        .flatMap(lambda r: mapper(r, cluster_size))

    # matrix = spark.read.csv(sys.argv[1], header=False, sep=";") \
    #     .rdd \
    #     .flatMap(mapper)

    vector = spark.read.csv(sys.argv[3], header=False, sep=";") \
        .rdd

    beta = 0.8
    confident = int(sys.argv[2])

    print(vector.collectAsMap())
    for _ in range(50):
        vector = vector \
            .map(lambda p: (int(int(p[0]) // cluster_size), (int(p[0]), float(p[1])))) \
            .join(matrix) \
            .map(lambda r: (r[1][1][0], (r[1][0][1] * r[1][1][2] if r[1][0][0] == r[1][1][1] else 0))) \
            .reduceByKey(lambda a, b: a + b) \
            .map(lambda p: (p[0], beta * p[1] + ((1 - beta) if p[0] == confident else 0)))

        print(vector.collectAsMap())

    # print(vector.collectAsMap())
    # for _ in range(50):
    #     vector = vector \
    #         .join(matrix) \
    #         .map(lambda r: (r[1][1][0], (r[1][0] * r[1][1][1]))) \
    #         .reduceByKey(lambda a, b: a + b) \
    #         .map(lambda p: (p[0], beta * p[1] + ((1 - beta) if p[0] == confident else 0)))
    #     print(vector.collectAsMap())

    spark.stop()
