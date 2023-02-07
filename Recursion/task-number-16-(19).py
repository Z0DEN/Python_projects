def f(n):
    if n <= 18:
        return n*n+3*n+5
    if n > 18 and n % 3 == 0:
        return (n // 3) * f(n // 3) + n - 12
    if n > 18 and n % 3 != 0:
        return f(n-1) + n * n + 5


#   k --- количество нулей в числе
#   a --- модуль значения функции от n
#   m --- количество чисел с 2-мя нулями


m = 0
for n in range(1, 801):
    a = abs(f(n))
    k = 0
    t = 0
    while a > 0:
        if ((a % 10) % 2) == 0:
            k += 1
        a //= 10
        t += 1
    if k == t:
        m += 1
print(m)
