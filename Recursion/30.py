from sys import *
setrecursionlimit(5000)


def f(n):
    if n <= 1:
        return n
    if n > 1:
        if n % 2 == 0:
            return 1 + f(n/2)
        return 0


#   k --- количество нулей в числе
#   a --- модуль значения функции от n
#   m --- количество чисел с 2-мя нулями

n = 0
while f(n) != 16:
        n += 1
print(n)
