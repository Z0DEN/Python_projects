from sys import *
setrecursionlimit(5000)

def f(n):
    if n <= 18:
        return n+3
    if n > 18 and n % 3 == 0:
        return (n // 3) * f(n // 3) + n - 12
    if n > 18 and n % 3 != 0:
        return f(n-1) + n * n + 5


#   k --- количество нулей в числе
#   a --- модуль значения функции от n
#   m --- количество чисел с 2-мя нулями


k = 0
flag = 0
count = 0
for n in range(1, 801):
    flag = 0
    k = 0
    a = abs(f(n))
    while a > 0:
        flag += 1
        if a % 10 % 2 != 0:
            break
        else:
            a //= 10
            k += 1
    if flag == k:
        count += 1
print("count -",count)
