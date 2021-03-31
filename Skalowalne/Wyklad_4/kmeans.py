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

    k = points.takeSample(False, 3)
    old_k = k.copy()
    itt = 0
    control = 1.0
    while round(control, 2) != 0.00:
        print("Obrot: " + str(itt))

        points_dist = points \
            .map(lambda p: (p[0], (p[1], k))) \
            .map(lambda p: (p[0], (p[1][0], [(t[0], distance(p[1][0], t[1])) for t in p[1][1]]))) \
            .map(lambda p: (p[0], (p[1][0], p[1][1][np.argmin(np.array(p[1][1])[:, 1])][0])))

        new_k = points_dist \
            .map(lambda p: (p[1][1], (p[1][0], 1))) \
            .reduceByKey(lambda a, b: ((a[0][0] + b[0][0], a[0][1] + b[0][1]), a[1] + b[1])) \
            .map(lambda p: (p[0], (p[1][0][0] / p[1][1], p[1][0][1] / p[1][1]))) \
            .collect()

        points = points_dist \
            .map(lambda p: (p[1][1], p[1][0]))

        k.sort(key=lambda p: p[0])
        new_k.sort(key=lambda p: p[0])

        control = sum([distance(i[1], j[1]) for i, j in zip(k, new_k)])

        k = new_k.copy()

        itt += 1

    points_draw = points.collect()
    colors = ['orange', 'cyan', 'magenta']
    np_points = np.stack(np.array(points_draw, dtype=object))

    for i in points_draw:
        print(i)

    for g, color in zip(k, colors):
        point = np.stack(np_points[np.where(np_points[:, 0] == g[0])][:, 1])
        plt.scatter(point[:, 0], point[:, 1], c=color)
        plt.scatter(g[1][0], g[1][1], c='black')
    plt.savefig("k-means.png")
    spark.stop()
