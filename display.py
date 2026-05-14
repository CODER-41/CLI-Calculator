from colorama import init, Fore, Style

#Initialize colorama
init(autoreset=True)

def print_header():
    print(Fore.CYAN + "CALCMASTER")
    print(Fore.CYAN + "CALCMASTER")
    print(Fore.CYAN + "CALCMASTER")
    print(Fore.CYAN + "CALCMASTER")
    print(Fore.CYAN + "CALCMASTER")
    print()

def print_success(message):
    print(Fore.GREEN + f"\n {message} \n")

def print_error(message):
    print(Fore.RED + f"\n {message} \n")

def print_prompt(message):
    return input(Fore.YELLOW + f"\n {message} \n")
    