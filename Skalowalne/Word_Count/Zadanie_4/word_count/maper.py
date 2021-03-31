#!/bin/python3
from sys import stdin, stdout
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
stopwords = set(open("word_count/english_stopwords.txt").read().split())

for line in stdin:
    tab = line.split()
    for i in tab:
        key = ''.join(e for e in i.lower() if e.isalnum())
        key = lemmatizer.lemmatize(key, 'n')
        if key not in stopwords and len(key) > 0:
            stdout.write(key + '\t' + '1\n')
