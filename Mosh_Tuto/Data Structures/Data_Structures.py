from sys import getsizeof  # import getsizeof to check memory size of objects
from array import array  # import array for efficient storage of same-type elements
# import deque for fast append/pop operations from both ends
from collections import deque

# ----------------------------
# Lists
# ----------------------------
# Lists are ordered, changeable, and allow duplicate members. Defined using square brackets []

letters = ['a', 'b', 'c', 'd']  # define a list of letters
print(type(letters))  # <class 'list'>
print(letters[0])  # access first element
print(letters[-1])  # access last element
print(letters[1:3])  # slicing, result: ['b','c']
letters[0] = 'z'  # modify first element
print(letters)  # ['z','b','c','d']

matrix = [[1, 2], [3, 4]]  # 2D list (list of lists)
zeros = [0] * 5  # create a list of five zeros
combined = letters + zeros  # concatenate two lists
numbers = list(range(5))  # create list of numbers from 0 to 4
chars = list("Hello World")  # create list of characters from string

# slicing examples
num = list(range(20))
print(num[::2])  # every second element
print(num[::-1])  # reverse list

# ----------------------------
# List unpacking
# ----------------------------
numbers = [5, 3, 8, 1, 2, 7, 4, 6, 0]
first, *others = numbers  # first element and rest of the list
first, second, *others, last = numbers  # unpacking multiple variables

# ----------------------------
# Looping over lists
# ----------------------------
letters = ['a', 'b', 'c', 'd']
for letter in letters:  # loop elements
    print(letter)

for index, letter in enumerate(letters):  # loop with index
    print(index, letter)

# ----------------------------
# Adding/Removing elements
# ----------------------------
letters.append('e')  # add at end
letters.insert(0, 'b')  # insert at index
letters.remove('b')  # remove first occurrence
letters.pop()  # remove last element
letters.pop(1)  # remove element at index
letters.index('c')  # find index
letters.clear()  # remove all elements
letters.count('a')  # count occurrences

# ----------------------------
# Sorting and reversing
# ----------------------------
letters = ['d', 'b', 'a', 'c']
letters.sort()  # ascending sort
letters.sort(reverse=True)  # descending sort
sorted(letters)  # returns a new sorted list without changing original

# Sorting with key functions
items = [("item1", 10), ("item2", 5), ("item3", 20)]
items.sort(key=lambda item: item[1])  # sort by second element

# List comprehensions
prices = [item[1] for item in items]  # extract second element
filtred = [item for item in items if item[1] >= 10]  # filter by condition

# Zip lists
liste1 = [1, 2, 3]
liste2 = [10, 20, 30]
combined = list(zip("ABC", liste1, liste2))  # combine into tuples

# ----------------------------
# Stack and Queue examples
# ----------------------------
browsing_session = []  # stack example using list
browsing_session.append("google.com")
browsing_session.pop()  # remove last

browsing_session = deque([])  # queue example using deque
browsing_session.append("google.com")
browsing_session.popleft()  # remove first element

# ----------------------------
# Tuples
# ----------------------------
point = (1, 2)  # tuple is ordered, immutable, allows duplicates
x, y = point  # unpack tuple
point*2  # repetition
x, y = y, x  # swap values

# ----------------------------
# Arrays
# ----------------------------
# array of integers, more memory efficient
numbers = array('i', [1, 2, 3, 4, 5])

# ----------------------------
# Sets
# ----------------------------
numbers = [1, 1, 2, 3, 4]
first = set(numbers)  # remove duplicates
second = {1, 5}
first | second  # union
first & second  # intersection
first - second  # difference
first ^ second  # symmetric difference
1 in first  # membership check

# ----------------------------
# Dictionaries
# ----------------------------
point = {"x": 1, "y": 2}
point["z"] = 20  # add new key
point.get("a")  # safe access, returns None if not exists
del point["x"]  # remove key

# Looping
for key, value in point.items():  # loop keys and values
    print(key, value)

# Dictionary comprehension
values = {x: x*2 for x in range(5)}  # create dictionary using comprehension

# ----------------------------
# Generator objects
# ----------------------------
values = (x*2 for x in range(100000))  # generator, memory efficient
getsizeof(values)  # small memory footprint
values_list = [x*2 for x in range(100000)]  # full list, large memory

# ----------------------------
# Unpacking operator
# ----------------------------
numbers = [1, 2, 3]
print(*numbers)  # unpack list into separate values
values = [*range(5), *"Hello"]  # combine iterables
# combine dictionaries, last key overrides
combined = {**{"x": 1}, **{"x": 23, "y": 5}, "z": 876}
