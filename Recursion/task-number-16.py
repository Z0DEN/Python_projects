def f(n):
    if n > 30:
        return n*n+3*n+5
    if n <= 30 and n % 2 == 0:
        return 2 * f(n+1) + f(n+4)
    if n <= 30 and n % 2 == 1:
        return f(n+2) + 3*f(n+5)


#   k --- количество нулей в числе
#   a --- модуль значения функции от n
#   m --- количество чисел с 2-мя нулями


m = 0
for n in range(1, 1001):
    a = abs(f(n))
    k = 0
    while a > 0:
        if a % 10 == 0:
            k += 1
        a //= 10
    if k > 2:
        m += 1
print(m)
