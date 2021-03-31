#!/usr/bin/env python3
from sys import stdin, stdout
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
stopwords = set(open("english_stopwords.txt").read().split())

output = []
for line in stdin:
    tab = line.split()
    for i in tab:
        key = ''.join(e for e in i.lower() if e.isalnum())
        key = lemmatizer.lemmatize(key, 'n')
        if key not in stopwords and len(key) > 0:
            output.append([key, 1])

output.sort(key=lambda tmp: tmp[0])

key = ''
value = 0
for _key, _value in output:
    if value == 0:
        value = int(_value)
        key = _key
    elif key != _key:
        stdout.write(key + '\t' + str(value) + '\n')
        value = int(_value)
        key = _key
    else:
        value += int(_value)
stdout.write(key + '\t' + str(value) + '\n')
