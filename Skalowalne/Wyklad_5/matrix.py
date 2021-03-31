#
#    Dawid Sikorski 291951
#

from __future__ import print_function

import sys
from pyspark.sql import SparkSession
import numpy as np

if __name__ == "__main__":
    """
        Usage: matrix.py [txt file with matrix A] [txt file with matrix B]
    """
    if len(sys.argv) != 3:
        print("Usage: matrix.py A.txt B.txt")
        sys.exit(-1)

    spark = SparkSession \
        .builder \
        .appName("Matrix") \
        .getOrCreate()

    matrixA = spark.read.text(sys.argv[1]) \
        .rdd \
        .map(lambda f: f[0].split(" ")) \
        .flatMap(lambda p: [((int(p[0]), i), int(p[i])) for i in range(1, len(p))]) \
        .map(lambda p: (p[0][1], (p[0][0], p[1])))

    matrixB = spark.read.text(sys.argv[2]) \
        .rdd \
        .map(lambda f: f[0].split(" ")) \
        .flatMap(lambda p: [((int(p[0]), i), int(p[i])) for i in range(1, len(p))]) \
        .map(lambda p: (p[0][0], (p[0][1], p[1])))

    matrixC = matrixA.join(matrixB) \
        .map(lambda p: ((p[1][0][0], p[1][1][0]), p[1][0][1] * p[1][1][1])) \
        .reduceByKey(lambda a, b: a + b)

    for i in matrixC.collect():
        print(i)

    spark.stop()
