from colorama import init, Fore
from colorama import Back
from colorama import Style

init(autoreset=True)


print(Fore.RED + Style.BRIGHT + 'Hello World')
Style.RESET_ALL