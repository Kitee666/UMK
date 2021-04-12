#
#    Dawid Sikorski 291951
#

from __future__ import print_function

import sys
from pyspark.sql import SparkSession
import numpy as np

if __name__ == "__main__":
    """
        Usage: forest_sensors.py [txt file with cords]
    """
    if len(sys.argv) != 2:
        print("Usage: forest_sensors.py [txt file with cords]")
        sys.exit(-1)

    spark = SparkSession \
        .builder \
        .appName("Forest sensors") \
        .getOrCreate()
    spark.sparkContext.setLogLevel("WARN")

    sensors = spark.read.text(sys.argv[1]) \
        .rdd \
        .map(lambda f: f[0].split(" ")) \
        .map(lambda p: (int(p[0]), int(p[1]))) \
        .filter(lambda p: 1 if p[0] < p[1] else 0)

    sensors_3_points = sensors \
        .join(sensors) \
        .filter(lambda p: 1 if p[1][0] < p[1][1] else 0) \
        .map(lambda p: (p[1][0], (p[0], p[1][1]))) \
        .join(sensors) \
        .filter(lambda p: 1 if p[1][0][1] == p[1][1] else 0) \
        .map(lambda p: ((p[1][0][0], p[0]), p[1][1]))

    sensors_4_points = sensors_3_points \
        .join(sensors_3_points) \
        #.filter(lambda p: 1 if p[1][0] < p[1][1] else 0) \
        #.map(lambda p: (p[1][0], (p[0], p[1][1]))) \
        #.join(sensors) \
        #.filter(lambda p: 1 if p[1][0][1] == p[1][1] else 0) \

    for i in sensors_3_points.collect():
        print(i)

    spark.stop()
