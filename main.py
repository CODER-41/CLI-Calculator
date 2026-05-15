# main.py
# Entry point for CalcMaster.
# Runs the main menu loop and routes the user to each calculator module.

from display import (print_header, print_error,
                     print_separator, clear_screen)
from history import view_history, clear_history
from scientific import run_scientific
from statistical import run_statistical
from colorama import Fore


def show_main_menu():
    # Prints the main menu with all available calculator options.
    print_header()
    print(Fore.CYAN + "  MAIN MENU\n")
    print(Fore.WHITE + "  1. Scientific Calculator")
    print(Fore.WHITE + "  2. Statistical Calculator")
    print(Fore.WHITE + "  3. Financial Calculator")
    print(Fore.WHITE + "  4. Unit Converter")
    print(Fore.WHITE + "  5. View History")
    print(Fore.WHITE + "  6. Clear History")
    print(Fore.RED   + "  0. Exit")
    print_separator()


def main():
    # The main application loop.
    # Keeps running until the user chooses to exit with option 0.
    while True:
        clear_screen()
        show_main_menu()

        choice = input(Fore.YELLOW + "\n  Enter your choice: ").strip()

        if choice == "1":
            run_scientific()

        elif choice == "2":
            run_statistical()

        elif choice == "3":
            print(Fore.YELLOW + "\n  Financial Calculator coming soon...\n")
            input(Fore.CYAN + "  Press Enter to go back to the main menu...")

        elif choice == "4":
            print(Fore.YELLOW + "\n  Unit Converter coming soon...\n")
            input(Fore.CYAN + "  Press Enter to go back to the main menu...")

        elif choice == "5":
            clear_screen()
            view_history()
            input(Fore.CYAN + "\n  Press Enter to go back to the main menu...")

        elif choice == "6":
            clear_history()
            input(Fore.CYAN + "  Press Enter to go back to the main menu...")

        elif choice == "0":
            print(Fore.CYAN + "\n  Thanks for using CalcMaster. Happy calculating!\n")
            break

        else:
            print_error("Invalid choice. Please enter a number from the menu.")
            input(Fore.CYAN + "  Press Enter to try again...")


# This block ensures main() only runs when this file is executed directly,
# not when it is imported as a module by another file.
if __name__ == "__main__":
    main()