from __future__ import print_function
import sys
from pyspark.sql import SparkSession


def Map(r):
    line = r.split("\t")
    if len(line) > 0:
        if line[0] == 'Orders':
            return [(line[2], (line[0], (line[1:])))]
        elif line[0] == 'Customers':
            return [(line[1], (line[0], (line[1:])))]
        else:
            return []
    return []


def Reduce(r):
    key, values = r[0], list(r[1])
    orders = []
    customers = []
    for v in values:
        if v[0] == 'Orders':
            orders.append(v)
        elif v[0] == 'Customers':
            customers.append(v)
    if len(customers) == 0:
        customers.append(('Customers', ['null', 'null', 'null', 'null']))
    customers_orders = [[c, o] for c in customers for o in orders]
    if len(customers_orders) > 0:
        return customers_orders
    else:
        return []


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: left_outer_join <file>", file=sys.stderr)
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonLeftOuterJoin") \
        .getOrCreate()
    spark.sparkContext.setLogLevel("WARN")

    lines = spark.read.text(sys.argv[1]) \
        .rdd \
        .map(lambda f: f[0])

    left_outer_join = lines \
        .flatMap(Map) \
        .groupByKey() \
        .flatMap(Reduce)

    for i in left_outer_join.collect():
        print(i)
    spark.stop()
