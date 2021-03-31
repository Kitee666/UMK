from __future__ import print_function
import sys
from operator import add
from pyspark.sql import SparkSession
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
stopwords = set(open("english_stopwords.txt").read().split())


def Map(r):
    line = r[0]
    output = []
    for i in line.split():
        key = ''.join(e for e in i.lower() if e.isalnum())
        key = lemmatizer.lemmatize(key, 'n')
        if key not in stopwords and len(key) > 0:
            output.append([key, 1])
    return output


def Reduce(r):
    key, value = r[0], r[1]
    return [key, sum(value)]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)
    spark = SparkSession \
        .builder \
        .appName("PythonWordCount") \
        .getOrCreate()
    lines = spark.read.text(sys.argv[1]).rdd
    countsR = lines.flatMap(Map) \
        .groupByKey() \
        .map(Reduce)

    for result in countsR.collect():
        print("Key = %s, value = %d" % (result[0], result[1]))
    spark.stop()
