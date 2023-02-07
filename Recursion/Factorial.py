<<<<<<< HEAD
from art import *
from colorama import init, Fore
from colorama import Back
from colorama import Style
from colorama import init
from termcolor import colored
init(autoreset=True)
Art = tprint('factorial')


def factorial(n):
=======
#from art import *
#Art = tprint("recursion")
n = input()


def f(n):
>>>>>>> 34e3262 (comm)
    if n == 1:
        return 1
    return n * f(n-1)


<<<<<<< HEAD
t = int(input(Fore.GREEN + Style.BRIGHT + 'введите число: '))
print (colored('{0:{width}}'.format('', width = 200)))
print(Fore.BLUE + Style.BRIGHT + 'факториал', colored('{0:{width}}'.format(t, width = 0), 'red'),Fore.BLUE + Style.BRIGHT + '=', colored('{0:{width}}'.format(factorial(t), width = 0), 'red'))
print (colored('{0:{width}}'.format('', width = 200)))
=======
print(f(n))
>>>>>>> 34e3262 (comm)
