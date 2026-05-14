# history.py
# Manages the session history for CalcMaster.
# History is stored in memory as a list of dictionaries
# and resets when the app exits — no file storage yet.

from display import print_separator
from colorama import Fore

# Our session history list — each entry is a dictionary
history = []


def add_to_history(category, operation, input_data, result):
    # Adds a new calculation entry to the history list.
    # Parameters:
    # - category: which calculator was used e.g "Scientific"
    # - operation: what was calculated e.g "Square Root"
    # - input_data: the inputs used e.g "25"
    # - result: the answer e.g "5.0"
    entry = {
        "id": len(history) + 1,
        "category": category,
        "operation": operation,
        "input": input_data,
        "result": result
    }
    history.append(entry)


def view_history():
    # Displays all calculations from the current session in a formatted table.
    print(Fore.CYAN + "\n  CALCULATION HISTORY\n")
    print_separator()

    if len(history) == 0:
        print(Fore.YELLOW + "  No calculations yet. Go crunch some numbers!\n")
    else:
        # Print the table header row
        print(Fore.CYAN + f"  {'#':<4} {'Category':<15} {'Operation':<20} {'Result'}")
        print_separator()
        # Print each history entry as a row
        for entry in history:
            print(Fore.WHITE + f"  {entry['id']:<4} {entry['category']:<15} {entry['operation']:<20} {entry['result']}")

    print_separator()


def clear_history():
    # Removes all entries from the history list.
    # list.clear() empties the list in place without creating a new one.
    history.clear()
    print(Fore.GREEN + "\n  History cleared!\n")