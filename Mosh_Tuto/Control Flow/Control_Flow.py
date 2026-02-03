# Boolean values
print(bool(0))     # False, 0 is considered False
print(bool(""))    # False, empty string is False
print(bool(None))  # False, None is False

# Comparison operators
# >  : greater than
# <  : less than
# >= : greater than or equal to
# <= : less than or equal to
# == : equal to
# != : not equal to
print(10 > 3)   # True
print(10 < 3)   # False
print(10 >= 3)  # True
print(10 <= 3)  # False
print(10 == 3)  # False
print(10 != 3)  # True

# String comparison (based on Unicode values)
print("bad" > "good")  # False
print("bad" < "good")  # True
print(ord("a"))         # 97, returns Unicode code point of character

# Conditional statements
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Multiple conditional branches
score = int(input("Enter your score: "))
if score >= 90:
    print("You got an A.")
elif score >= 80:
    print("You got a B.")
elif score >= 70:
    print("You got a C.")
elif score >= 60:
    print("You got a D.")
else:
    print("You got an F.")

# Ternary (conditional) operator
message = "eligible" if age >= 18 else "not eligible"
print(message)

# Logical operators
a = True
b = False
c = False

if a and b:  # both must be true
    print("Azul!")
if a or b:   # at least one must be true
    print("Hi!")
if (a and b) or not c:  # combination of operators
    print("Salut!")
if a and b and c:  # short-circuit: stops evaluating after first False
    print("SalamAleykoum!")
if a or b or c:  # short-circuit: stops evaluating after first True
    print("hola!")

# Chained comparison
age = 25
if 10 <= age <= 60:  # checks if age is between 10 and 60 inclusive
    print("Valid age")

# For loops
for number in range(5):         # loop from 0 to 4
    print(number)
for number in range(2, 6):      # loop from 2 to 5
    print(number)
for number in range(2, 10, 2):  # loop 2,4,6,8 (step of 2)
    print(number)
for char in "Hello":             # iterate through each character
    print(char)
for item in [1, 2, 3, 4, 5]:    # iterate through each list element
    print(item)

# For loop with break
for i in range(5):
    if i == 3:
        break  # exit the loop when i is 3
    print(i)
else:
    print("Loop ended without break")  # executes only if loop was not broken

# Nested for loops
for i in range(5):
    for j in range(3):
        print(f"i: {i}, j: {j}")  # nested loop example

# While loops
# Loop until user types "exit" (case-insensitive)
comand = ""
while comand.lower() != "exit":
    comand = input("> : ")
    print(f"You entered: {comand}")

# Infinite while loop with break
while True:
    comand = input("> : ")
    if comand.lower() == "exit":  # exit condition
        break
    print(f"You entered: {comand}")
