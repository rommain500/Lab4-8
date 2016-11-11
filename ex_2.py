#!/usr/bin/env python3

from librip.iterators import Unique
from librip.gens import gen_random

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['a', 'A', 'b', 'B']
data4 = ['юрист', 'Юрист ']

# Реализация задания 2

u = Unique(data1)
for i in u:
    print(i, end=" ")
print()

u = Unique(data2)
for i in u:
    print(i, end=" ")
print()

u = Unique(data3)
for i in u:
    print(i, end=" ")
print()

u = Unique(data4, ignore_case = True)
for i in u:
    print(i, end=" ")
