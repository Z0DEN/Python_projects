from art import *
from colorama import init, Fore
from colorama import Back
from colorama import Style
init(autoreset=True)
Art = tprint('factorial')


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


t = int(input(Fore.GREEN + Style.BRIGHT + 'введите число: '))
print(factorial(t))
