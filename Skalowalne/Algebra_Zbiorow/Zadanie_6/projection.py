from __future__ import print_function
import sys
from pyspark.sql import SparkSession


def Map(r, header):
    # ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'credit_card_type', 'currency', 'job_title',
    # 'company name', 'country', 'shirt_size', 'income']

    return r, tuple(r[header.index(i)] for i in ['id', 'first_name', 'last_name', 'company name'])


def Reduce(r):
    key, value = r[0], r[1]
    return list(value)[0]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: projection <file>", file=sys.stderr)
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonProjection") \
        .getOrCreate()
    spark.sparkContext.setLogLevel("WARN")

    lines = spark \
        .read \
        .option("header", True) \
        .csv(sys.argv[1])

    header = [i.name for i in lines.schema.fields]

    projection = lines \
        .rdd \
        .map(tuple) \
        .map(lambda s: Map(s, header)) \
        .groupByKey() \
        .map(Reduce)

    for i in projection.collect():
        print(i)

    spark.stop()
