from __future__ import print_function
import sys
from pyspark.sql import SparkSession

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: matrix_vector.py [matrixA_0.csv] ...", file=sys.stderr)
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonMatrixVectorSmall") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    vector = [2, -3, 0, 9, 1, 2, 2, 0, 1]

    out = []
    for i in range(1, len(sys.argv)):
        out.append(spark.read.csv(sys.argv[i], sep=";")
                   .rdd
                   .map(lambda r: (int(r[0]), float(r[2]) * float(vector[int(r[1])])))
                   )

    k = 0
    for i in out:
        k += 1
        print('Part', k)
        for j in i.collect():
            print(j)

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
