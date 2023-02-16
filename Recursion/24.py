def f(n):
    if n < 4:
        return n-1
    if n >= 4 and n % 3 == 0:
        return n + 2 * f(n-1)
    if n >= 4 and n % 3 != 0:
        return f(n-2) + f(n-3)


#   k --- количество нулей в числе
#   a --- модуль значения функции от n
#   m --- количество чисел с 2-мя нулями


k = 0
def summa(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum


print (summa(f(25)))
