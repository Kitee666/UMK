from __future__ import print_function
import sys
from pyspark.sql import SparkSession

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: matrix_vector.py directory_matrix directory_vector number_of_clusters", file=sys.stderr)
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonMatrixVector") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    vector_dir = sys.argv[2]
    cluster_size = int(sys.argv[3])

    current_cluster = -1
    vector = {}


    def multiply(r):
        global current_cluster
        global vector
        row, col, val = int(r[0]), int(r[1]), float(r[2])
        if int(col // cluster_size) != current_cluster:
            current_cluster = int(col // cluster_size)
            file = open(vector_dir + 'vector_' + str(current_cluster) + '.csv', 'r').readlines()
            for line in file:
                line_st = line.strip().split(';')
                vector[int(line_st[0])] = float(line_st[1])
        if col in vector:
            return [(row, val * vector[col])]
        return []


    out = spark.sparkContext.textFile(sys.argv[1]) \
        .map(lambda line: line.strip().split(';')) \
        .flatMap(multiply) \
        .reduceByKey(lambda a, b: a + b)

    for i in out.collect():
        print(i)

    # Wersja 2

    # out = spark.sparkContext \
    #     .union([
    #     spark.read.csv(sys.argv[i], sep=";") \
    #         .rdd \
    #         .map(lambda r: (int(r[1]), (int(r[0]), float(r[2])))) \
    #         .join(spark.read.csv(sys.argv[i + 1], sep=";") \
    #               .rdd \
    #               .map(lambda r: [(int(r[0])), float(r[1])])
    #               ) \
    #         .map(lambda r: (r[1][0][0], r[1][0][1] * r[1][1]))
    #     for i in range(1, len(sys.argv), 2)
    # ]).reduceByKey(lambda a, b: a + b)
    #
    # for i in out.collect():
    #     print(i)
