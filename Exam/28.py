def f(n):
    if n < 50:
        return n
    if n > 49:
        return 2 * g(50-n//2)


def g(n):
    if n > 40:
        return 10
    if n < 41:
        return 30 + f(n+600//n)


#   k --- количество нулей в числе
#   a --- модуль значения функции от n
#   m --- количество чисел с 2-мя нулями


print(f(80))
