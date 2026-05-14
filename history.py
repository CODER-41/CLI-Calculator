#Manages the session history for CalcMaster

from display import print_separator
from colorama import Fore

#Our sesssion history list - each entry is a dictionary
history = []

def add_to_history(category, operation, input_data, result):
    # Adds a new calculation enrty to the history list
    # parameters:
    # -category: which calculator was used e.g scientific
    # -operation: what operation was performed e.g addition
    # -input_data: the numbers used in the calculation
    # -result: the result of the calculation
    entry = {
        'id': len(history) + 1,
        'category': category,
        'operation': operation,
        'input': input_data,
        'result': result
    }
    history.append(entry)

def view_history():
    # Displays all calculations from the current session in  a formatted table
    print(Fore.CYAN + "\n CALCULATION  HISTORY\n")
    print_separator()

    if len(history) == 0:
        print(Fore.YELLOW + 'No calculations yet')
    else:
        # print the table header row
        print(Fore.CYAN  + f" {'#':<4} {'category':<15} {'operation':<20} {'Result'}")
        print_separator()
        
        # Print each history entry as a row
        for entry in history:
            print(Fore.WHITE + f" {entry['id']:<4} {entry['category']:<15} {entry['operation']:<20} {entry['result']}")
    
    print_separator()


    def clear_history():
        # Removes all entries from the history list
        # list.clear() empties the list in place without creating a new one
        history.clear()
        print(Fore.GREEN + "\n istory Cleared!\n")