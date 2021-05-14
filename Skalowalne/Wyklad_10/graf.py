#
#    Dawid Sikorski 291951
#

from __future__ import print_function

import sys
from pyspark.sql import SparkSession
import numpy as np

if __name__ == "__main__":
    """
        Usage: graf.py [txt file with edges]
    """
    if len(sys.argv) != 2:
        print("Usage: graf.py graf.txt")
        sys.exit(-1)

    spark = SparkSession \
        .builder \
        .appName("Graf") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    edges = spark.read.text(sys.argv[1]) \
        .rdd \
        .map(lambda f: f[0].split()) \
        .flatMap(lambda p: [(int(p[0]), int(p[1])), (int(p[1]), int(p[0]))])

    vert = edges \
        .reduceByKey(lambda a, b: a) \
        .map(lambda p: (p[0]))

    # Krok 0
    blue = vert \
        .map(lambda p: (p, p)) \
        .cache()

    check = 1
    while check > 0:
        # Krok 1
        # Do kazdego wierzcholka dopisujemy polaczenia,
        # zmieniamy kolejnosc i laczymy aby wiedziec na co wskazuje,
        # robimy minimum na co wskazywal z tym na co wskazywal sasiad
        # i redukujemy zeby miec minimum
        green = blue \
            .join(edges) \
            .map(lambda p: (p[1][1], (p[0], p[1][0]))) \
            .join(blue) \
            .map(lambda p: (p[1][0][0], min(p[1][0][1], p[1][1]))) \
            .reduceByKey(lambda a, b: min(a, b)) \

        # Krok 2
        # Przechodzimy dalej po wskazywany
        orange = green \
            .map(lambda p: (p[1], p[0])) \
            .join(green) \
            .map(lambda p: (p[1][0], p[1][1])) \

        # Krok 3
        # Sprawdzenie ilosci zmian
        check = blue \
            .join(orange) \
            .map(lambda p: 1 if p[1][0] != p[1][1] else 0) \
            .sum()

        print("Ilosc zmian: ", check)

        blue = orange.cache()

    print("Zbieram wynik...")
    out = blue \
        .collect()
    out.sort()
    for i in out:
        print(i)
    # # Krok 1_2
    # green2 = orange \
    #     .join(edges) \
    #     .map(lambda p: (p[1][1], (p[0], p[1][0]))) \
    #     .join(orange) \
    #     .map(lambda p: (p[1][0][0], min(p[1][0][1], p[1][1]))) \
    #     .reduceByKey(lambda a, b: min(a, b)) \
    #     .cache()
    #
    # # Krok 2
    # orange2 = green2 \
    #     .map(lambda p: (p[1], p[0])) \
    #     .join(green2) \
    #     .map(lambda p: (p[1][0], p[1][1])) \
    #     .cache()
    #
    # print("Krok niebieski")
    # out = blue.collect()
    # out.sort()
    # for i in out:
    #     print(i)
    #
    # print("Krok zielony")
    # out = green.collect()
    # out.sort()
    # for i in out:
    #     print(i)
    #
    # print("Krok pomaranczowy")
    # out = orange.collect()
    # out.sort()
    # for i in out:
    #     print(i)
    #
    # print("Krok zielony 2")
    # out = green2.collect()
    # out.sort()
    # for i in out:
    #     print(i)
    #
    # print("Krok pomaranczowy 2")
    # out = orange2.collect()
    # out.sort()
    # for i in out:
    #     print(i)
