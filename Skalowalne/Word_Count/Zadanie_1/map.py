#!/usr/bin/env python3
from sys import stdin, stdout

for line in stdin:
    tab = line.split()
    for i in tab:
        stdout.write(i + '\t' + '1\n')
