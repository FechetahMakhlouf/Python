from pprint import pprint
# Write a Python program that prints all even numbers from 1 to 9 and counts how many even numbers there are.
count = 0
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
        count += 1
print(f"we have {count} even numbers")

# Write a Python function that takes an integer as input and returns "fizz" if the number is divisible by 3,
# "buzz" if it is divisible by 5, "fizz_buzz" if it is divisible by both 3 and 5, and the number itself if it is divisible by neither.


def fizz_buzz(input_numbr):
    if (input_numbr % 3 == 0) and (input_numbr % 5 == 0):
        return "fizz_buzz"
    if input_numbr % 5 == 0:
        return "buzz"
    if input_numbr % 3 == 0:
        return "fizz"

    return input_numbr


print(fizz_buzz(15))

# Write a program to find the most repeted caracter in the text
text = "this is a common interview question"
char_rep = {}
for char in text:
    if char in char_rep:
        char_rep[char] += 1
    else:
        char_rep[char] = 1
pprint(char_rep, width=1)  # width=1 that's mean 1 character in the line

char_rep_sorted = sorted(char_rep.items(),
                         key=lambda kv: kv[1],
                         reverse=True)
print(char_rep_sorted)
print(f"the most repeted char is {char_rep_sorted[0]}")
