# ----------------------------
# Functions in Python
# ----------------------------

# Define a function that performs a task
def greet(first_name, last_name):  # function with two parameters
    # perform a task (print)
    print(f"Hello {first_name} {last_name}, welcome to the program!")


# Call the function with arguments
greet("Fechetah", "Makhlouf")
# Output: Hello Fechetah Makhlouf, welcome to the program!

# ----------------------------
# Function that returns a value
# ----------------------------


def greeting(name):
    return f"Hello {name}!"  # return a value instead of printing


# Call the function and store its return value
message = greeting("Makhlouf")
print(message)  # Output: Hello Makhlouf!

# ----------------------------
# Function with multiple parameters
# ----------------------------


def increment(number, by):
    return number + by


print(increment(5, 2))        # Output: 7
print(increment(10, by=5))    # Output: 15  # using keyword argument

# ----------------------------
# Function with default parameter value
# ----------------------------


def default_increment(number, by=1):  # default value must be last
    return number + by


print(default_increment(5))       # Output: 6  (by=1 default)
print(default_increment(5, 3))    # Output: 8  (override default)

# ----------------------------
# Function with variable number of arguments (*args)
# ----------------------------


def multiply(*numbers):  # *numbers collects all positional arguments into a tuple
    result = 1
    for number in numbers:
        print(number)      # print each number
        result *= number   # multiply all numbers together
    return result


print(multiply(2, 3, 4, 5))  # Output: 120

# ----------------------------
# Function with variable keyword arguments (**kwargs)
# ----------------------------


def save_user(**user_info):  # **user_info collects keyword arguments into a dictionary
    print(user_info["id"])    # access value by key
    print(user_info["name"])  # access value by key
    print(user_info["age"])   # access value by key
    print(user_info)          # print full dictionary


# Call function with keyword arguments
save_user(id=1, name="Makhlouf", age=22)

# ----------------------------
# Variable scope and global keyword
# ----------------------------
text = "b"  # global variable


def change_text():
    global text    # declare we want to modify the global variable
    text = "a"     # modify the global variable


change_text()
print(text)  # Output: "a"

# ----------------------------
# Debugging shortcuts in VS Code
# ----------------------------
# F9  : toggle breakpoint
# F5  : start debugging
# F10 : step over
# F11 : step into
# Shift+F11 : step out
# Shift+F5  : stop debugging

# ----------------------------
# Editor shortcuts in VS Code
# ----------------------------
# Ctrl + /           : comment/uncomment a line
# Alt + Up/Down Arrow: move a line up/down
# Shift + Alt + Up/Down Arrow: copy a line up/down
# Ctrl + D           : select next occurrence of selected word
# Ctrl + Shift + L   : select all occurrences of selected word
# Ctrl + .           : show quick fixes
# Ctrl + Shift + O   : go to symbol
# Ctrl + P           : quickly open a file
# End key            : move to end of line
# Home key           : move to beginning of line
