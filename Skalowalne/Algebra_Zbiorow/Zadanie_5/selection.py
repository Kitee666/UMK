from __future__ import print_function
import sys
from pyspark.sql import SparkSession


def Map(r, header, column, operation, value):
    # ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'credit_card_type', 'currency', 'job_title',
    # 'company name', 'country', 'shirt_size', 'income']
    index = header.index(column)
    if operation == '=' and r[index] == value:
        return [r]
    if operation == '>' and int(r[index]) > int(value):
        return [r]
    if operation == '<' and int(r[index]) < int(value):
        return [r]
    if operation == '>=' and int(r[index]) >= int(value):
        return [r]
    if operation == '<=' and int(r[index]) <= int(value):
        return [r]
    if operation == '!=' and r[index] != value:
        return [r]
    if operation == 'like' and value in r[index].lower():
        return [r]
    return []
    # index = header.index('id')
    # if 3 < int(r[index]) < 10:
    #     return [r]

    # index = header.index('gender')
    # if r[index] == 'Female':
    #     return [r]

    # index = header.index('first_name')
    # if 'ala' in r[index].lower():
    #     return [r]
    #
    # return []


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: selection <file> <column> <operation> <value>", file=sys.stderr)
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonSelection") \
        .getOrCreate()
    spark.sparkContext.setLogLevel("WARN")

    lines = spark \
        .read \
        .option("header", True) \
        .csv(sys.argv[1])

    header = [i.name for i in lines.schema.fields]

    column = sys.argv[2]
    operation = sys.argv[3]
    value = sys.argv[4]

    selection = lines \
        .rdd \
        .map(tuple) \
        .flatMap(lambda s: Map(s, header, column, operation, value))

    for i in selection.collect():
        print(i)

    spark.stop()
