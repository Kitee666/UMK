#
#    Dawid Sikorski 291951
#

from __future__ import print_function

import sys
from pyspark.sql import SparkSession
import numpy as np
import matplotlib.pyplot as plt


def distance(a, b):
    return np.sqrt(np.sum(np.square(np.array(a) - np.array(b))))


if __name__ == "__main__":
    """
        Usage: kmeans.py [txt file with points { format: id[int] x[float] y[float]}]
    """
    if len(sys.argv) != 2:
        print("Usage: kmeans.py points.txt")
        sys.exit(-1)

    spark = SparkSession \
        .builder \
        .appName("Kmeans") \
        .getOrCreate()

    points = spark.read.text(sys.argv[1]) \
        .rdd \
        .map(lambda f: f[0].split(" ")) \
        .map(lambda p: (int(p[0]), (float(p[1]), float(p[2]))))

    k = spark \
        .sparkContext \
        .parallelize(points.takeSample(False, 3))

    check = 0
    last = 1
    points_calc = []
    while last != check:
        # (id, (x,y)) => (id, ((x, y), (k1, (x[k1],y[k1])))
        points_dist = points \
            .cartesian(k) \
            .map(lambda p: (p[0], (p[1][0], distance(p[0][1], p[1][1])))) \
            .reduceByKey(lambda v1, v2: v1 if v1[1] < v2[1] else v2)
        # ((id, (x,y)),(k, odl))
        last = check
        check = points_dist \
            .map(lambda p: p[1][1]) \
            .sum()

        points_calc = points_dist \
            .map(lambda p: (p[1][0], p[0][1]))

        k = points_calc \
            .map(lambda p: (p[0], (p[1], 1))) \
            .reduceByKey(lambda v1, v2: ((v1[0][0] + v2[0][0], v1[0][1] + v2[0][1]), v1[1] + v2[1])) \
            .map(lambda p: (p[0], (p[1][0][0] / p[1][1], p[1][0][1] / p[1][1])))

    groups = k.collect()
    points = points_calc.collect()
    colors = ['orange', 'cyan', 'magenta']
    np_points = np.stack(np.array(points, dtype=object))

    for g, color in zip(groups, colors):
        point = np.stack(np_points[np.where(np_points[:, 0] == g[0])][:, 1])
        plt.scatter(point[:, 0], point[:, 1], c=color)
    plt.savefig("k-means.png")

    spark.stop()
