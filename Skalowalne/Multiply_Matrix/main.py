# TODO Zrobic podzial matrix na plaster i wektor

# TODO Wczytywac katalog z plikami w rdd
# TODO vektor to slownik rzadka

# from __future__ import print_function
# import sys
# from pyspark.sql import SparkSession
#
# if __name__ == "__main__":
#     if len(sys.argv) != 1:
#         print("Usage: main.py", file=sys.stderr)
#         exit(-1)
#
#     spark = SparkSession \
#         .builder \
#         .appName("PythonTest") \
#         .getOrCreate()
#
#     spark.sparkContext.setLogLevel("WARN")
#
#     out = spark.sparkContext.textFile("Dane")
#
#     outWithName = spark.sparkContext.wholeTextFiles("Dane").map(lambda p: test())
#
#     for i in outWithName.collect():
#         print(i)