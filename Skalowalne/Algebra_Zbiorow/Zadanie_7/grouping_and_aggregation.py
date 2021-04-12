from __future__ import print_function
import sys
from pyspark.sql import SparkSession
import numpy as np

def Map(r, header, a, b):
    # ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'credit_card_type', 'currency', 'job_title',
    # 'company name', 'country', 'shirt_size', 'income']

    return r[header.index(a)], r[header.index(b)]


def Reduce(r):
    key, value = r[0], r[1]
    values = [float(i[1:]) for i in value]
    return key, 'sum $' + str(np.sum(values)), 'mean $' + str(np.mean(values)) \
        , 'count ' + str(len(values)), 'min ' + str(min(values)), 'max' + str(max(values))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: grouping_and_aggregation <file>", file=sys.stderr)
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonGroupingAndAggregation") \
        .getOrCreate()
    spark.sparkContext.setLogLevel("WARN")

    lines = spark \
        .read \
        .option("header", True) \
        .csv(sys.argv[1])

    header = [i.name for i in lines.schema.fields]

    a = sys.argv[2]
    b = sys.argv[3]

    grouping_and_aggregation = lines \
        .rdd \
        .map(tuple) \
        .map(lambda s: Map(s, header, a, b)) \
        .groupByKey() \
        .map(Reduce)

    for i in grouping_and_aggregation.collect():
        print(i)

    spark.stop()
