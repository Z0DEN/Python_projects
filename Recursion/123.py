from colorama import init
from termcolor import colored
init()
print (colored('{0:{width}}'.format('', width = 500)))
print (colored('{0:{width}}'.format('Hello World!', width = 500), 'green'))
print (colored('{0:{width}}'.format('Hi!', width = 0), 'green'))
print (colored('{0:{width}}'.format('', width = 500)))