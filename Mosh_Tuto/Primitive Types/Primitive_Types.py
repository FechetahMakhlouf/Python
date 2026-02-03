import math  # import the math module to use mathematical functions

# Strings
long_message = """Hi my name is Makhlouf I am learning Python programming language."""  # multi-line string
short_message = "hello world"  # single-line string

# Data types
boolean_value = True  # boolean value
float_number = 10.5  # floating-point number
integer_number = 5   # integer number

# String operations
print(len(long_message))       # print the length of the string
print(short_message[0])        # print first character: 'h'
print(short_message[-1])       # print last character: 'd'
print(short_message[0:3])      # print substring from index 0 to 2: 'hel'
# print substring from index 0 to end: 'hello world'
print(short_message[0:])
print(short_message[:3])       # print substring from start to index 2: 'hel'
print(short_message[:])        # print whole string: 'hello world'

# Escape characters
print("\"Hel\'lo \nWo\\rld")
# \" = double quote
# \' = single quote
# \\ = backslash
# \n = new line

# String concatenation
first_name = "Makhlouf"
last_name = "Fechetah"
full_name = first_name + " " + last_name
print(full_name)  # "Makhlouf Fechetah"

# f-string formatting
full_name = f"A {first_name} B {last_name} C"
print(full_name)  # "A Makhlouf B Fechetah C"

# String methods
course = "Python Programming"
print(course.upper())        # convert to uppercase: "PYTHON PROGRAMMING"
print(course.lower())        # convert to lowercase: "python programming"
print(course.find("Pro"))    # find substring starting index: 7
# replace substring: "Java Programming"
print(course.replace("Python", "Java"))
print("Python" in course)    # check if substring exists: True
print("python" not in course)  # check if substring does not exist: True
# capitalize first letter of each word: "Python Programming"
print(course.title())
# capitalize first letter of string: "Python programming"
print(course.capitalize())

# Strip whitespace
whitespace_string = "   Hello World   "
# remove spaces from start and end: "Hello World"
print(whitespace_string.strip())

# Arithmetic operations
print(10 + 3)   # addition: 13
print(10 - 3)   # subtraction: 7
print(10 * 3)   # multiplication: 30
print(10 / 3)   # division (float): 3.3333...
print(10 // 3)  # floor division: 3
print(10 % 3)   # modulus (remainder): 1
print(10 ** 3)  # exponentiation: 1000
print(10 + 3 * 2)  # operator precedence: 16
print((10 + 3) * 2)  # parentheses first: 26

# Augmented assignment operators
x = 10
x += 3  # x = x + 3
print(x)

x = 10
x *= 3  # x = x * 3
print(x)

x = 10
x -= 3  # x = x - 3
print(x)

x = 10
x /= 3  # x = x / 3 (float division)
print(x)

x = 10
x %= 3  # x = x % 3
print(x)

x = 10
x **= 3  # x = x ** 3
print(x)

x = 10
x //= 3  # x = x // 3
print(x)

# Math functions
print(round(10.6))      # round to nearest integer: 11
print(abs(-10))          # absolute value: 10
print(math.ceil(10.2))   # ceiling: 11
print(math.floor(10.8))  # floor: 10
print(math.sqrt(16))     # square root: 4.0
print(math.pow(2, 3))    # power: 8.0
print(max(10, 3))        # maximum: 10
print(min(10, 3))        # minimum: 3
print(math.pi)           # value of pi: 3.141592653589793

# Input and type conversion
x = input("Enter a number: ")  # input returns string by default
print(type(x))                  # <class 'str'>
x = int(x)                      # convert string to integer
print(type(x))                  # <class 'int'>

y = x + 5
print(f"x: {x}, y: {y}")        # f-string to display values

# Converting data types
int(x)    # convert to integer
float(x)  # convert to float
str(x)    # convert to string
bool(x)   # convert to boolean
