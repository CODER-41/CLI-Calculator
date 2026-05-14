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


def print_result(operation, result):
    print()
    print(Fore.CYAN  + "RESULT")
    print(Fore.CYAN  + "RESULT")
    print(Fore.CYAN  + "RESULT")
    print(Fore.GREEN + f" {operation} = {result} ")
    print(Fore.CYAN + "RESULT")
    print()

    def print_separator():
        print(Fore.CYAN + " ")
    
    def clear_screen():
        print("\n" * 2)