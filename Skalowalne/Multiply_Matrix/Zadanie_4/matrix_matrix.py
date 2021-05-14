from __future__ import print_function
import sys
from pyspark.sql import SparkSession

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: matrix_matrix.py matrixA.csv matrixB.csv", file=sys.stderr)
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonMatrixMatrix") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    matrixA = spark.read.csv(sys.argv[1], sep=";") \
        .rdd \
        .map(lambda r: (int(r[1]), (int(r[0]), float(r[2]))))

    matrixB = spark.read.csv(sys.argv[2], sep=";") \
        .rdd \
        .map(lambda r: (int(r[0]), (int(r[1]), float(r[2]))))

    out = matrixA \
        .join(matrixB) \
        .map(lambda r: ((r[1][0][0], r[1][1][0]), r[1][0][1] * r[1][1][1])) \
        .reduceByKey(lambda a, b: a + b)

    for i in out.collect():
        print(i)
