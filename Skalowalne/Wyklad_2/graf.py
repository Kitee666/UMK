
#
#    Dawid Sikorski 291951
#

from __future__ import print_function

import sys
import time
from pyspark.sql import SparkSession

if __name__ == "__main__":
    """
        Usage: graph.py [txt file with graph] [txt file with questions]
    """
    if len(sys.argv) != 3:
        print("Usage: graf.py input_graph.txt questions.txt")
        sys.exit(-1)

    spark = SparkSession \
        .builder \
        .appName("Graph") \
        .getOrCreate()
    start = time.time()

    input_graph = spark.read.text(sys.argv[1]) \
        .rdd \
        .map(lambda f: f[0])

    edges = input_graph \
        .map(lambda line: line.split(" ")) \
        .flatMap(lambda edge: [edge, (edge[1], edge[0])])

    input_questions = spark.read.text(sys.argv[2]) \
        .rdd \
        .map(lambda f: f[0])

    questions = input_questions \
        .map(lambda line: line.split(" ")) \
        .map(lambda edge: ((edge[0], edge[1]), 0))

    vertices = edges \
        .reduceByKey(lambda a, b: a) \
        .map(lambda edge: edge[0])

    BFS = vertices \
        .map(lambda vert: (vert, (0, vert)))

    limit = 0
    limit2 = BFS.count()
    while limit != limit2:
        limit = limit2
        BFS = BFS.union(BFS \
                        .join(edges) \
                        .map(lambda node: (node[1][1][0], (node[1][0][0] + 1, node[1][0][1])))) \
            .map(lambda tmp: ((tmp[1][1], tmp[0]), tmp[1][0])) \
            .reduceByKey(lambda dist_a, dist_b: min(dist_a, dist_b)) \
            .map(lambda tmp: (tmp[0][1], (tmp[1], tmp[0][0])))
        limit2 = BFS.count()

    connect = BFS \
        .map(lambda tmp: ((tmp[1][1], tmp[0]), tmp[1][0])) \
        .join(questions) \
        .map(lambda tmp: ((tmp[0][0], tmp[0][1]), max(tmp[1][0], tmp[1][1])))
    no_connect = questions.subtractByKey(connect) \
        .map(lambda tmp: ((tmp[0][0], tmp[0][1]), "No_connect"))

    out_connections = BFS \
        .map(lambda tmp: ((tmp[1][1], tmp[0]), tmp[1][0])) \
        .collect()
    out_questions = questions.collect()
    out_connect = connect.collect()
    out_no_connect = no_connect.collect()

    print("Polaczenie pomiedzy wierzcholkami oraz minimalna odleglosc")
    for i in out_connections:
        print(i)
    print("Zapytania z istniejaca droga")
    for i in out_connect:
        print(i)
    print("Zapytania z brakiem drogi")
    for i in out_no_connect:
        print(i)
    print("Time: %s" % (time.time() - start))
    spark.stop()
