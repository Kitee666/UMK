#!/usr/bin/env python3
from sys import stdin, stdout

key = ''
value = 0
# zmienic wczytanie poczatkowe
for line in stdin:
    tab = line.split()
    if value == 0:
        value = int(tab[1])
        key = tab[0]
    elif key != tab[0]:
        stdout.write(key + '\t' + str(value) + '\n')
        value = int(tab[1])
        key = tab[0]
    else:
        value += int(tab[1])
stdout.write(key + '\t' + str(value) + '\n')
