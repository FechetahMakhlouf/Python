# ----------------------------
# Handling Different Exceptions
# ----------------------------

from timeit import timeit  # used to measure execution time of code snippets

try:
    # Opening files using a context manager ("with" statement)
    # Automatically closes the files even if an exception occurs
    # FileNotFoundError is NOT caught here because it’s not listed in the except block
    with open("Exceptions/Exceptions.py") as file, open("exercice.py") as exercice:
        print("Files opened successfully.")

    # Ask the user for age and convert input to integer
    # If input is invalid (like "abc") → ValueError
    age = int(input("Age : "))

    # Attempt to divide by age
    # If age is 0 → ZeroDivisionError
    xfactor = 10 / age

except (ValueError, ZeroDivisionError) as ex:
    # This block only catches ValueError and ZeroDivisionError
    print("You didn't enter a valid age.")  # friendly message
    print(ex)  # prints the exact error message
    print(type(ex))  # prints the type of the exception

else:
    # Runs ONLY if no exception occurred in try block
    print("No exception was thrown.")

# No finally needed here because "with" automatically closes files

print("Execution continues")  # code always runs after try/except

# ----------------------------
# Raising Exceptions Manually
# ----------------------------


def calculat_Xfactor(age):
    """
    Compute x-factor based on age.
    Raise ValueError if age is invalid (<= 0)
    """
    if age <= 0:
        # "raise" creates and throws an exception intentionally
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculat_Xfactor(-1)  # will raise ValueError
except ValueError as error:
    # catches ValueError and prints the message
    print(error)

# ----------------------------
# Comparing Performance: Exceptions vs Return Values
# ----------------------------

# CODE 1: Using exceptions (slower)
code_1 = """
def calculat_Xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")  # raising exception is costly
    return 10 / age

try:
    calculat_Xfactor(-1)  # triggers exception
except ValueError as error:
    pass  # ignore exception
"""

# CODE 2: Using "None" instead of exceptions (faster)
code_2 = """
def calculat_Xfactor(age):
    if age <= 0:
        return None  # simple and fast
    return 10 / age

Xfactor = calculat_Xfactor(-1)
if Xfactor is None:  # recommended to use 'is None'
    pass
"""

# Measure execution time for each approach
print("First code  : ", timeit(code_1, number=10000000))
print("Second code : ", timeit(code_2, number=10000000))
