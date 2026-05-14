from colorama import init, Fore, Style

#Initialize colorama
init(autoreset=True)

def print_header():
    #prints a simple styled CalcMaster title at the head of the scren
    print()
    print(Fore.CYAN + Style.BRIGHT +  " CALCMASTER")
    print(Fore.CYAN + " ------------------")
   
    print()

def print_success(message):
    print(Fore.GREEN + f"\n {message} \n")

def print_error(message):
    print(Fore.RED + f"\n {message} \n")

def print_prompt(message):
    return input(Fore.YELLOW + f"\n {message} \n")


def print_result(operation, result):
    print()
    print(Fore.CYAN  + " ------------------")
    print(Fore.CYAN  + " RESULT")
    print(Fore.CYAN  + " ------------------")
    print(Fore.GREEN + f" {operation} = {result} ")
    print(Fore.CYAN + " -------------------")
    print()


def print_separator():
    #Prints a simple horixontal line to visually separate sections on screen
        print(Fore.CYAN + " ")
    
def clear_screen():
        print("\n" * 2)