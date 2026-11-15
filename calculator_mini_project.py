
import math
import json
import os
from datetime import datetime

# ==========================================
# STAGE 1: BASIC CALCULATOR
# STAGE 2: SCIENTIFIC CALCULATOR
# STAGE 3: HISTORY, UNDO AND REPEAT
# STAGE 4: ERROR HANDLING
# STAGE 5: SAVE AND LOAD HISTORY
# ==========================================

HISTORY_FILE = "calculator_history.json"

history = []
last_result = None
last_calculation = None


# ---------- STAGE 1: BASIC OPERATIONS ----------

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot calculate modulus with zero.")
    return a % b


def floor_division(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot perform floor division by zero.")
    return a // b


def power(a, b):
    return a ** b


# ---------- STAGE 2: SCIENTIFIC OPERATIONS ----------

def square_root(a):
    if a < 0:
        raise ValueError("Square root of a negative number is not supported.")
    return math.sqrt(a)


def square(a):
    return a ** 2


def cube(a):
    return a ** 3


def factorial(a):
    if a < 0 or not a.is_integer():
        raise ValueError("Factorial requires a non-negative integer.")
    return math.factorial(int(a))


def sine(a):
    return math.sin(math.radians(a))


def cosine(a):
    return math.cos(math.radians(a))


def tangent(a):
    if math.isclose(a % 180, 90, abs_tol=1e-10):
        raise ValueError("Tangent is undefined at this angle.")
    return math.tan(math.radians(a))


def logarithm(a):
    if a <= 0:
        raise ValueError("Logarithm requires a positive number.")
    return math.log10(a)


def natural_log(a):
    if a <= 0:
        raise ValueError("Natural logarithm requires a positive number.")
    return math.log(a)


def percentage(a):
    return a / 100


def reciprocal(a):
    if a == 0:
        raise ZeroDivisionError("Reciprocal of zero is undefined.")
    return 1 / a


# ---------- OPERATION DETAILS ----------

# Each entry stores the function and number of inputs.
OPERATIONS = {
    "add": (add, 2),
    "subtract": (subtract, 2),
    "multiply": (multiply, 2),
    "divide": (divide, 2),
    "modulus": (modulus, 2),
    "floor_division": (floor_division, 2),
    "power": (power, 2),

    "square_root": (square_root, 1),
    "square": (square, 1),
    "cube": (cube, 1),
    "factorial": (factorial, 1),
    "sin": (sine, 1),
    "cos": (cosine, 1),
    "tan": (tangent, 1),
    "log": (logarithm, 1),
    "ln": (natural_log, 1),
    "percentage": (percentage, 1),
    "reciprocal": (reciprocal, 1)
}


# ---------- STAGE 5: FILE HANDLING ----------

def load_history():
    global history, last_result, last_calculation

    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as file:
                history = json.load(file)

            if not isinstance(history, list):
                history = []

            if history:
                last_result = history[-1]["result"]
                last_calculation = history[-1]

            print("Previous calculation history loaded.")

        except (json.JSONDecodeError, OSError, KeyError, TypeError):
            history = []
            last_result = None
            last_calculation = None
            print("Could not load old history. Starting fresh.")


def save_history():
    try:
        with open(HISTORY_FILE, "w") as file:
            json.dump(history, file, indent=4)

    except OSError:
        print("Warning: Could not save calculation history.")


# ---------- STAGE 3: CALCULATION HISTORY ----------

def show_history():
    if not history:
        print("\nNo calculation history available.")
        return

    print("\n========== CALCULATION HISTORY ==========")

    for index, item in enumerate(history, start=1):
        print(
            f"{index}. {item['expression']} = {item['result']}"
        )

    print("=========================================")


def undo_last():
    global last_result, last_calculation

    if not history:
        print("Nothing to undo.")
        return

    removed = history.pop()

    if history:
        last_result = history[-1]["result"]
        last_calculation = history[-1]
    else:
        last_result = None
        last_calculation = None

    save_history()

    print("Removed:", removed["expression"])
    print("Last result restored:", last_result)


def repeat_last():
    if last_calculation is None:
        print("No previous calculation to repeat.")
        return

    operation = last_calculation["operation"]
    operands = last_calculation["operands"]

    print("\nRepeating:", last_calculation["expression"])
    perform_calculation(operation, operands)


# ---------- INPUT HANDLING ----------

def get_number(message):
    while True:
        value = input(message).strip().lower()

        if value == "ans":
            if last_result is None:
                print("There is no previous result.")
                continue
            return float(last_result)

        try:
            return float(value)
        except ValueError:
            print("Invalid input. Enter a number or 'ans'.")


# ---------- CALCULATION ENGINE ----------

def perform_calculation(operation, operands):
    global last_result, last_calculation

    try:
        function, expected_inputs = OPERATIONS[operation]

        if len(operands) != expected_inputs:
            print("Incorrect number of inputs.")
            return

        result = function(*operands)

        # Prevent storing non-finite results.
        if isinstance(result, float) and not math.isfinite(result):
            raise ValueError("The result is too large or undefined.")

        expression = operation + "(" + ", ".join(
            str(value) for value in operands
        ) + ")"

        record = {
            "operation": operation,
            "operands": operands,
            "result": result,
            "expression": expression,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        history.append(record)
        last_result = result
        last_calculation = record

        save_history()

        print("\nResult:", result)

    except (ValueError, ZeroDivisionError, OverflowError) as error:
        print("Calculation error:", error)

    except Exception as error:
        print("Unexpected error:", error)


# ---------- MENU ----------

def display_menu():
    print("\n========== SMART CALCULATOR ==========")

    print("\n1.  Addition")
    print("2.  Subtraction")
    print("3.  Multiplication")
    print("4.  Division")
    print("5.  Modulus")
    print("6.  Floor Division")
    print("7.  Power")

    print("\n--- SCIENTIFIC OPERATIONS ---")
    print("8.  Square Root")
    print("9.  Square")
    print("10. Cube")
    print("11. Factorial")
    print("12. Sine (Degrees)")
    print("13. Cosine (Degrees)")
    print("14. Tangent (Degrees)")
    print("15. Logarithm (Base 10)")
    print("16. Natural Logarithm")
    print("17. Percentage")
    print("18. Reciprocal")

    print("\n--- SMART FEATURES ---")
    print("19. View History")
    print("20. Undo Last Calculation")
    print("21. Repeat Last Calculation")
    print("22. Show Previous Result")
    print("23. Exit")

    print("======================================")


# ---------- MAIN PROGRAM ----------

def main():
    load_history()

    while True:
        display_menu()

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 23:
                save_history()
                print("Thank you for using Smart Calculator!")
                break

            elif choice == 19:
                show_history()
                continue

            elif choice == 20:
                undo_last()
                continue

            elif choice == 21:
                repeat_last()
                continue

            elif choice == 22:
                print("Previous result:", last_result)
                continue

            # Map menu choices to operation names.
            menu_operations = {
                1: "add",
                2: "subtract",
                3: "multiply",
                4: "divide",
                5: "modulus",
                6: "floor_division",
                7: "power",
                8: "square_root",
                9: "square",
                10: "cube",
                11: "factorial",
                12: "sin",
                13: "cos",
                14: "tan",
                15: "log",
                16: "ln",
                17: "percentage",
                18: "reciprocal"
            }

            if choice not in menu_operations:
                print("Invalid menu choice. Try again.")
                continue

            operation = menu_operations[choice]
            _, number_of_inputs = OPERATIONS[operation]

            operands = []

            for index in range(number_of_inputs):
                number = get_number(
                    f"Enter number {index + 1} (or 'ans'): "
                )
                operands.append(number)

            perform_calculation(operation, operands)

        except ValueError:
            print("Please enter a valid menu number.")


# Start the calculator.
if __name__ == "__main__":
    main()


"""
output :

========== SMART CALCULATOR ==========

1.  Addition
2.  Subtraction
3.  Multiplication
4.  Division
5.  Modulus
6.  Floor Division
7.  Power

--- SCIENTIFIC OPERATIONS ---
8.  Square Root
9.  Square
10. Cube
11. Factorial
12. Sine (Degrees)
13. Cosine (Degrees)
14. Tangent (Degrees)
15. Logarithm (Base 10)
16. Natural Logarithm
17. Percentage
18. Reciprocal

--- SMART FEATURES ---
19. View History
20. Undo Last Calculation
21. Repeat Last Calculation
22. Show Previous Result
23. Exit
======================================

Enter your choice: 8
Enter number 1 (or 'ans'): 34

Result: 5.830951894845301

========== SMART CALCULATOR ==========

1.  Addition
2.  Subtraction
3.  Multiplication
4.  Division
5.  Modulus
6.  Floor Division
7.  Power

--- SCIENTIFIC OPERATIONS ---
8.  Square Root
9.  Square
10. Cube
11. Factorial
12. Sine (Degrees)
13. Cosine (Degrees)
14. Tangent (Degrees)
15. Logarithm (Base 10)
16. Natural Logarithm
17. Percentage
18. Reciprocal

--- SMART FEATURES ---
19. View History
20. Undo Last Calculation
21. Repeat Last Calculation
22. Show Previous Result
23. Exit
======================================

Enter your choice: 12
Enter number 1 (or 'ans'): 90 

Result: 1.0

========== SMART CALCULATOR ==========

1.  Addition
2.  Subtraction
3.  Multiplication
4.  Division
5.  Modulus
6.  Floor Division
7.  Power

--- SCIENTIFIC OPERATIONS ---
8.  Square Root
9.  Square
10. Cube
11. Factorial
12. Sine (Degrees)
13. Cosine (Degrees)
14. Tangent (Degrees)
15. Logarithm (Base 10)
16. Natural Logarithm
17. Percentage
18. Reciprocal

--- SMART FEATURES ---
19. View History
20. Undo Last Calculation
21. Repeat Last Calculation
22. Show Previous Result
23. Exit
======================================

Enter your choice: 23
Thank you for using Smart Calculator!
"""
