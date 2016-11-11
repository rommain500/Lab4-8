#!/usr/bin/env python3
import json
import sys
#import codecs
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique
print(sys.getdefaultencoding())
#sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer, 'replace')
#sys.stderr = codecs.getwriter('utf8')(sys.stderr.buffer, 'replace')

path = sys.argv[1]

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path, encoding="cp1251") as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(arg):

    return sorted(unique([i for i in field(arg, 'job-name')], ignore_case=1), key=lambda x:x.lower())

@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith("Программист"),arg))


@print_result
def f3(arg):
    return list(map(lambda x: x+" с опытом Python", arg))


@print_result
def f4(arg):
    s = list(gen_random(100000, 200000, len(arg)))
    return list('{}, зарплата {} руб.'.format(arg,s) for arg,s in zip (arg,s))


with timer():
     f4(f3(f2(f1(data))))
