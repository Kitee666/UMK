from __future__ import print_function
import sys
from operator import add
from pyspark.sql import SparkSession

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)
    spark = SparkSession \
        .builder \
        .appName("PythonWordCount") \
        .getOrCreate()
    #spark.sparkContext.setLogLevel("WARN")
    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    countsR = lines.pipe("./word_count/maper.py") \
        .sortBy(lambda line: line.split("\t")[0]) \
        .pipe("./word_count/reducer.py")

    for line in countsR.collect():
        print("%s" % line)
    spark.stop()
