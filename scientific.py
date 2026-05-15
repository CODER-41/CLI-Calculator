# Handles all scientific calculations for CalcMaster
# Covers Basic arithmetic, power, squareroot, logarithms

import math
from colorama import Fore
from display import print_result, print_error, print_separator, clear_screen
from history import add_to_history


# Basic Arithmetic

def add(a, b):
    # return sum of two numbers
    return a + b

def subtract(a, b):
    # return difference of two numbers
    return a - b

def multiply(a, b):
    # return product of two numbers
    return a * b

def divide(a,b):
    # return the quotient of two numbers
    # raises ValueError when user tries to divide by zero
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


# POWER AND ROOTS
def power(base, exp):
    # returns base raised to the power of exp
    return math.pow(base, exp)

def square_root(a):
    # returns a square root of a number
    # raises ValueError when user tries to take the square root of a negative number
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)


# LOGARITHMS
def log_base10(a):
    # returns the base -10 logarithm of a number 
    # raises a ValueError for zero or negative numbers
    if a <= 0:
        raise ValueError("Logarithm is undefined for zero or negative numbers.")
    return math.log10(a)

def natural_log(a):
    # Returns the natural logarithm (base e ) of a number
    # Raises Value error for zero or negative numbers
    if a <= 0:
        raise ValueError("Logarithm is undefined for zero or negative numbers.")
    return math.log(a)

# TRIGONOMETRY

def sine(degrees):
    # Returns the sine of an angle in degrees
    return math.sin(math.radians(degrees))

def cosine(degrees):
    # Returns the cosine of an angle in degrees
    return math.cos(math.radians(degrees))

def tangent(degrees):
    # Returns the tangent of an angle in degrees
    # Raises a ValueError at angles where tangent is undefined(90, 270, etc.)
    if degrees % 180 == 90:
        raise ValueError("Tangent is undefined at this angle.")
    return math.tan(math.radians(degrees))

# FACTORIAL AND MODULUS
def factorial(n):
    # Returns the factorial of a non-negative integer
    # e.g factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
    # Raises a ValueError for negative numbers and non-integers
    
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    if not float(n).is_integer():
        raise ValueError("Factorial is only defined for whole numbers.")
    return math.factorial(int(n))

def modulus(a, b):
    # Returns the remainder when a is divided by b
    # e.g modulus(5, 2) = 5 % 2 = 1
    # Raises a ValueError when b is zero
    if b == 0:
        raise ValueError("cannot perfom modulus with zero as the divisor.")   
    return a % b

# INPUT HELPER
def get_number(prompt):
    # A reusable helper that prompts the user for a number
    # And keeps asking until a valid number is entered
    # This is the try/except pattern in action -the backbone
    # of all input validation
    while True:
        try:
            return float(input(Fore.YELLOW + f" {prompt}: "))
        except ValueError:
            print_error("Invalid input. Please enter a number.")

# SUB-MENU
def show_scientific_menu():
    # Prints the scientific calculator sub-menu
    clear_screen()
    print(Fore.CYAN + "  SCIENTIFIC CALCULATOR")
    print_separator()
    print(Fore.WHITE + "  1.  Addition")
    print(Fore.WHITE + "  2.  Subtraction")
    print(Fore.WHITE + "  3.  Multiplication")
    print(Fore.WHITE + "  4.  Division")
    print(Fore.WHITE + "  5.  Power")
    print(Fore.WHITE + "  6.  Square Root")
    print(Fore.WHITE + "  7.  Log Base 10")
    print(Fore.WHITE + "  8.  Natural Log")
    print(Fore.WHITE + "  9.  Sine")
    print(Fore.WHITE + "  10. Cosine")
    print(Fore.WHITE + "  11. Tangent")
    print(Fore.WHITE + "  12. Factorial")
    print(Fore.WHITE + "  13. Modulus")
    print(Fore.RED   + "  0.  Back to Main Menu")
    print_separator()
 
 
def run_scientific():
    # The main loop for the scientific calculator.
    # Keeps running until the user enters 0 to go back.
    while True:
        show_scientific_menu()
        choice = input(Fore.YELLOW + "\n  Enter your choice: ").strip()
 
        try:
            if choice == "1":
                a = get_number("Enter first number")
                b = get_number("Enter second number")
                result = add(a, b)
                print_result(f"{a} + {b}", result)
                add_to_history("Scientific", "Addition", f"{a}, {b}", result)
 
            elif choice == "2":
                a = get_number("Enter first number")
                b = get_number("Enter second number")
                result = subtract(a, b)
                print_result(f"{a} - {b}", result)
                add_to_history("Scientific", "Subtraction", f"{a}, {b}", result)
 
            elif choice == "3":
                a = get_number("Enter first number")
                b = get_number("Enter second number")
                result = multiply(a, b)
                print_result(f"{a} x {b}", result)
                add_to_history("Scientific", "Multiplication", f"{a}, {b}", result)
 
            elif choice == "4":
                a = get_number("Enter the dividend (number to divide)")
                b = get_number("Enter the divisor (number to divide by)")
                result = divide(a, b)
                print_result(f"{a} / {b}", result)
                add_to_history("Scientific", "Division", f"{a}, {b}", result)
 
            elif choice == "5":
                base = get_number("Enter the base")
                exp = get_number("Enter the exponent")
                result = power(base, exp)
                print_result(f"{base} ^ {exp}", result)
                add_to_history("Scientific", "Power", f"{base}, {exp}", result)
 
            elif choice == "6":
                a = get_number("Enter a number")
                result = square_root(a)
                print_result(f"sqrt({a})", result)
                add_to_history("Scientific", "Square Root", f"{a}", result)
 
            elif choice == "7":
                a = get_number("Enter a number")
                result = log_base10(a)
                print_result(f"log10({a})", result)
                add_to_history("Scientific", "Log Base 10", f"{a}", result)
 
            elif choice == "8":
                a = get_number("Enter a number")
                result = natural_log(a)
                print_result(f"ln({a})", result)
                add_to_history("Scientific", "Natural Log", f"{a}", result)
 
            elif choice == "9":
                a = get_number("Enter angle in degrees")
                result = sine(a)
                print_result(f"sin({a})", round(result, 6))
                add_to_history("Scientific", "Sine", f"{a} deg", round(result, 6))
 
            elif choice == "10":
                a = get_number("Enter angle in degrees")
                result = cosine(a)
                print_result(f"cos({a})", round(result, 6))
                add_to_history("Scientific", "Cosine", f"{a} deg", round(result, 6))
 
            elif choice == "11":
                a = get_number("Enter angle in degrees")
                result = tangent(a)
                print_result(f"tan({a})", round(result, 6))
                add_to_history("Scientific", "Tangent", f"{a} deg", round(result, 6))
 
            elif choice == "12":
                a = get_number("Enter a number")
                result = factorial(a)
                print_result(f"{int(a)}!", result)
                add_to_history("Scientific", "Factorial", f"{a}", result)
 
            elif choice == "13":
                a = get_number("Enter the dividend")
                b = get_number("Enter the divisor")
                result = modulus(a, b)
                print_result(f"{a} mod {b}", result)
                add_to_history("Scientific", "Modulus", f"{a}, {b}", result)
 
            elif choice == "0":
                # Break out of the loop and return to the main menu
                break
 
            else:
                print_error("Invalid choice. Please enter a number from the menu.")
 
        except ValueError as e:
            # Catches errors raised by our functions e.g division by zero,
            # square root of negative, etc. and shows a friendly message
            print_error(str(e))
 
        input(Fore.CYAN + "  Press Enter to continue...")
 