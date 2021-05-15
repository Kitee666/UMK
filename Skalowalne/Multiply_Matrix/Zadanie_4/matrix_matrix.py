from __future__ import print_function
import sys
from pyspark.sql import SparkSession


def reducer(row):
    row_a = list(filter(lambda r: r[0] == 'A', row[1]))
    col_b = list(filter(lambda r: r[0] == 'B', row[1]))
    row_a.sort(key=lambda it: it[1])
    col_b.sort(key=lambda it: it[1])
    j = 0
    i = 0
    out = 0.0
    while i < len(row_a) and j < len(col_b):
        if row_a[i][1] > col_b[j][1]:
            j += 1
        elif row_a[i][1] < col_b[j][1]:
            i += 1
        else:
            out += row_a[i][2] * col_b[j][2]
            i += 1
            j += 1
    if out != 0.0:
        return [(row[0], out)]
    return []


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: matrix_matrix.py directory_matrix_A directory_matrix_B number_columns_B number_rows_A", file=sys.stderr)
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonMatrixMatrix") \
        .getOrCreate()

    cols_B = int(sys.argv[3])
    rows_A = int(sys.argv[4])

    spark.sparkContext.setLogLevel("WARN")

    matrixA = spark.sparkContext.textFile(sys.argv[1]) \
        .map(lambda line: line.strip().split(';')) \
        .flatMap(lambda r: [((int(r[0]), k + 1), ('A', int(r[1]), float(r[2]))) for k in range(cols_B)])

    matrixB = spark.sparkContext.textFile(sys.argv[2]) \
        .map(lambda line: line.strip().split(';')) \
        .flatMap(lambda r: [((i + 1, int(r[1])), ('B', int(r[0]), float(r[2]))) for i in range(rows_A)])

    matrixC = matrixA.union(matrixB) \
        .groupByKey() \
        .flatMap(reducer)

    for j in matrixC.collect():
        print(j)

    # matrixA = spark.read.csv(sys.argv[1], sep=";") \
    #     .rdd \
    #     .map(lambda r: (int(r[1]), (int(r[0]), float(r[2]))))
    #
    # matrixB = spark.read.csv(sys.argv[2], sep=";") \
    #     .rdd \
    #     .map(lambda r: (int(r[0]), (int(r[1]), float(r[2]))))
    #
    # out = matrixA \
    #     .join(matrixB) \
    #     .map(lambda r: ((r[1][0][0], r[1][1][0]), r[1][0][1] * r[1][1][1])) \
    #     .reduceByKey(lambda a, b: a + b)
    #
    # for i in out.collect():
    #     print(i)
