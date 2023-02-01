from art import *
Art = text2art("factorial", font='block', chr_ignore=True)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(input("введите число")))