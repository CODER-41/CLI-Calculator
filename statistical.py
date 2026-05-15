import statistics
from colorama import Fore
from display import print_result, print_error, print_separator, clear_screen
from history import add_to_history

# INPUT HELPER

def get_number():
    # Prompts the user to enter a series of numbers separated by commas.
    # Splits the string, converts each item to a float and returns a list
    # keeps asking until the user enters at least two valid numbers 

    while True:
        try:
            raw = input (Fore.YELLOW + " Enter numbers separated by commas e.g(4,8)")
            # split() breaks the string at each comma into a list of strings
            # float()converts each string piece into a float
            numbers = [float(n.strip()) for n in raw.split(",")]
            if len(numbers) < 2:
                print_error("Please enter at least two numbers.")
                continue
            return numbers
        except ValueError:
            print_error("Invalid input. Please enter numbers separated by commas.")
        
# STATISTICAL FUNCTIONS
def calc_mean(numbers):
    # Returns the average of a list of numbers 
    # sum() adds them all up, len() countts how many are there
    return sum(numbers) / len(numbers)

def calc_median(numbers):
    # Returns the middle value when the numbers are sorted
    # uses the built in statistics module to handle both odd and even lists correctly
    return statistics.median(numbers)

def calc_mode(numbers):
    # Returns the most common value in the list
    # Raises StatisticsError if there is no single mode
    return statistics.mode(numbers)

def calc_stdev(numbers):
    # Returns the standard deviation of a list of numbers: a measure of how spread out the numbers are from the mean
    return statistics.stdev(numbers)

def calc_variance(numbers):
    # Returns the Variance: the average of squared differences from the mean. Variance is the square of standard deviation

    return statistics.variance(numbers)

def calc_min(numbers):
    # returns the smallest number in the list
    return min(numbers)

def calc_max(numbers):
    # returns the largest number in the list
    return max(numbers)

def calc_sum(numbers):
    # Returns the sum of all numbers in the list
    return sum(numbers)

def calc_range(numbers):
    # Returns the difference between the largest and smallest numbers in the list
    return max(numbers) - min(numbers)

# SUB-MENU
def show_statistical_menu():
    # Prints the statistical calculator sub-menu
    clear_screen()
    print(Fore.CYAN + "  STATISTICAL CALCULATOR")
    print_separator()
    print(Fore.WHITE + "  1. Mean (Average)")
    print(Fore.WHITE + "  2. Median")
    print(Fore.WHITE + "  3. Mode")
    print(Fore.WHITE + "  4. Standard Deviation")
    print(Fore.WHITE + "  5. Variance")
    print(Fore.WHITE + "  6. Minimum")
    print(Fore.WHITE + "  7. Maximum")
    print(Fore.WHITE + "  8. Sum")
    print(Fore.WHITE + "  9. Range")
    print(Fore.RED   + "  0. Back to Main Menu")
    print_separator()
 
 
def run_statistical():
    # The main loop for the statistical calculator.
    # Keeps running until the user enters 0 to go back.
    while True:
        show_statistical_menu()
        choice = input(Fore.YELLOW + "\n  Enter your choice: ").strip()
 
        if choice == "0":
            break
 
        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print_error("Invalid choice. Please enter a number from the menu.")
            input(Fore.CYAN + "  Press Enter to continue...")
            continue
 
        # All operations need a list of numbers so we collect them once here
        numbers = get_number()
 
        try:
            if choice == "1":
                result = calc_mean(numbers)
                print_result("Mean", round(result, 4))
                add_to_history("Statistical", "Mean", str(numbers), round(result, 4))
 
            elif choice == "2":
                result = calc_median(numbers)
                print_result("Median", result)
                add_to_history("Statistical", "Median", str(numbers), result)
 
            elif choice == "3":
                result = calc_mode(numbers)
                print_result("Mode", result)
                add_to_history("Statistical", "Mode", str(numbers), result)
 
            elif choice == "4":
                result = calc_stdev(numbers)
                print_result("Standard Deviation", round(result, 4))
                add_to_history("Statistical", "Std Deviation", str(numbers), round(result, 4))
 
            elif choice == "5":
                result = calc_variance(numbers)
                print_result("Variance", round(result, 4))
                add_to_history("Statistical", "Variance", str(numbers), round(result, 4))
 
            elif choice == "6":
                result = calc_min(numbers)
                print_result("Minimum", result)
                add_to_history("Statistical", "Minimum", str(numbers), result)
 
            elif choice == "7":
                result = calc_max(numbers)
                print_result("Maximum", result)
                add_to_history("Statistical", "Maximum", str(numbers), result)
 
            elif choice == "8":
                result = calc_sum(numbers)
                print_result("Sum", result)
                add_to_history("Statistical", "Sum", str(numbers), result)
 
            elif choice == "9":
                result = calc_range(numbers)
                print_result("Range", result)
                add_to_history("Statistical", "Range", str(numbers), result)
 
        except statistics.StatisticsError as e:
            # Catches cases like no unique mode existing in the data
            print_error(str(e))
 
        input(Fore.CYAN + "  Press Enter to continue...")
