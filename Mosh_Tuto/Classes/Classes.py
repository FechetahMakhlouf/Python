from collections import namedtuple
from abc import ABC, abstractmethod

# Class : Blueprint for creating new object
# Object : instance of a class

# Class : Human
# Object : Makhlouf , Jack...


class Point:  # Class names use PascalCase by convention

    # Class attribute (shared by ALL instances of this class)
    default_color = "red"

    @classmethod
    def zero(cls):

        # Class method:
        # - Receives the class itself as the first argument (cls), not the instance (self).
        # - Used to create alternative constructors.
        # This method returns a new Point object located at (0, 0).
        # Equivalent to Point(0, 0), but works correctly with inheritance.
        return cls(0, 0)

    def __init__(self, x, y):

        # Constructor (__init__):
        # - Runs automatically when creating a new object.
        # - 'self' refers to the current instance.

        self.x = x  # Instance attribute
        self.y = y  # Instance attribute

    def __str__(self):
        return f"({self.x}, {self.y})"

        # __str__ is a magic method that defines how the object is
        # represented as a string.

        # Called when you use print(obj) or str(obj).

        # Without __str__, Python prints something like:
        # <__main__.Point object at 0x...>

    def __eq__(self, other):

        # Magic method __eq__:
        # - Defines how two objects are compared using ==
        # - Two points are equal if both x and y are equal

        return self.x == other.x and self.y == other.y

    def __gt__(self, other):

        # Magic method __gt__:
        # - Defines behavior of > operator
        # - Here: a point is 'greater' if its x AND y are both larger

        return self.x > other.x and self.y > other.y

    def __add__(self, other):

        # Magic method __add__:
        # - Defines + operator between two points
        # - Adds x together and y together

        return Point(self.x + other.x, self.y + other.y)

    def draw(self):

        # Instance method:
        # - Operates on the object (self).
        # - Prints the coordinates of the point.

        print(f"Point ({self.x}, {self.y})")


# Creating an object (instance) of the Point class
point_1 = Point(1, 2)

print(type(point_1))             # <class '__main__.Point'>
print(isinstance(point_1, Point))  # True

# Calling an instance method
point_1.draw()

# Creating another instance
point_2 = Point(3, 4)

# Accessing the class attribute
print(Point.default_color)     # red  (accessed from the class)
print(point_2.default_color)   # red  (inherited from the class)

# Changing the class attribute — affects all objects
Point.default_color = "Yellow"

print(Point.default_color)     # Yellow
print(point_2.default_color)   # Yellow

# Using the class method to create a "special" object at (0, 0)
point_3 = Point.zero()
point_3.draw()                 # Point (0, 0)


# Magic methods (searchable on python.org)

point_4 = Point(44, 23)
print(point_4)                        # Calls __str__ → (44, 23)

# __eq__ comparison
print(point_1 == point_2)  # False

# __gt__ comparison
print(point_2 > point_1)  # True

# Using __add__
print(str(point_1 + point_2))  # (4, 6)

# Saving the result of addition
point_combined = point_1 + point_2

# Accessing attributes of the new Point
print(point_combined.x, point_combined.y)  # 4 6


# Making custom containers

class TagCloud1:
    # Constructor: initializes an empty dictionary to store tags
    def __init__(self):
        self.tags = {}

    # Adds a tag (case-insensitive). Converts to lowercase and increments its count.
    def add(self, tag):
        # Convert the tag to lowercase and increase its count.
        # If the tag doesn't exist, start the count at 1.
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    # Allows access using cloud["python"]
    def __getitem__(self, tag):
        # Return the count of the tag (case-insensitive). If not found, return 0.
        return self.tags.get(tag.lower(), 0)

    # Allows assignment using cloud["python"] = 10
    def __setitem__(self, tag, count):
        # Set the count of the tag, converting the tag to lowercase.
        self.tags[tag.lower()] = count

    # Returns the number of unique tags stored
    def __len__(self):
        # Return how many unique tags exist in the dictionary.
        return len(self.tags)

    # Makes the object iterable (e.g., for tag in cloud)
    def __iter__(self):
        # Allow iteration over the dictionary keys.
        return iter(self.tags)


# Creating a TagCloud object
cloud_1 = TagCloud1()

# Adding tags (case-insensitive because of .lower())
cloud_1.add("Python")
cloud_1.add("PythoN")
cloud_1.add("Java")
cloud_1.add("C++")

# Print the internal dictionary of tags
print(cloud_1.tags)

# Access the count of a specific tag
print(cloud_1["python"])

# Manually modify the count of a tag
cloud_1["python"] = 10

# Print the dictionary after modification
print(cloud_1.tags)

# Print the number of unique tags
print(len(cloud_1))


# Private members

class TagCloud2:
    # Constructor: initializes an empty dictionary to store tags
    def __init__(self):
        # __tags is a *private* attribute (name-mangled by Python)
        self.__tags = {}

    # Adds a tag (case-insensitive). Converts to lowercase and increments its count.
    def add(self, tag):
        # Same behavior as TagCloud1 but stored in a private dictionary
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    # Allows access using cloud["python"]
    def __getitem__(self, tag):
        # Return the tag count or 0 if it does not exist
        return self.__tags.get(tag.lower(), 0)

    # Allows assignment using cloud["python"] = 10
    def __setitem__(self, tag, count):
        # Modify the tag count (case-insensitive)
        self.__tags[tag.lower()] = count

    # Returns the number of unique tags stored
    def __len__(self):
        # Return how many unique tags are in the private dictionary
        return len(self.__tags)

    # Makes the object iterable (e.g., for tag in cloud)
    def __iter__(self):
        # Iterate over the private dictionary keys
        return iter(self.__tags)


# Creating a TagCloud object
cloud_2 = TagCloud2()

# Show internal attributes of the object
# Note: __tags becomes _TagCloud2__tags due to name mangling
print(cloud_2.__dict__)

# Adding tags (case-insensitive because of .lower())
cloud_2.add("Python")
cloud_2.add("Java")
cloud_2.add("C++")
cloud_2.add("JS")

# Print the internal dictionary of tags (accessed via name mangling)
print(cloud_2._TagCloud2__tags)

# Access the count of a specific tag
print(cloud_2["python"])

# Manually modify the count of a tag
cloud_2["python"] = 10

# Print the dictionary after modification
print(cloud_2._TagCloud2__tags)

# Print the number of unique tags
print(len(cloud_2))


# Demonstration of the @property decorator in Python

class Product:
    def __init__(self, price):
        # When we assign self.price, Python automatically calls the setter method (price.setter)
        # instead of setting an attribute directly.
        self.price = price

    @property
    def price(self):

        # @property turns this method into a 'getter'.
        # This allows us to access the value like an attribute:
        #     prod.price
        # instead of calling it like a function:
        #     prod.price()

        # The getter is used whenever you READ the value.

        return self.__price  # Return the private attribute

    @price.setter
    def price(self, value):

        # @price.setter defines the 'setter' for the price property.
        # The setter is automatically called whenever you ASSIGN a value:
        #     prod.price = 50

        # It allows us to add validation or logic before updating the value.

        if value < 0:
            # Here we validate the data. Negative prices are not allowed.
            raise ValueError("Price cannot be negative.")

        # If validation passes, store the value in a private variable.
        # We use __price to protect it from direct modification.
        self.__price = value


# Create a product with a valid price (calls the setter)
prod_1 = Product(10)
print(prod_1.price)  # Calls the getter

# If we tried: Product(-3), the setter would throw an error because -3 is invalid.
# prod_2 = Product(-3)  # Example of invalid price

# Valid product
prod_2 = Product(3)

# Update the price (this calls the setter)
prod_2.price = 2000

# Read the price (this calls the getter)
print(prod_2.price)

# Inheritance
# DRY = Don't Repeat Yourself (reuse code instead of rewriting it)


class Animal:
    def __init__(self):
        # This is the constructor of Animal.
        # It runs first *if* called using super() inside a child class.
        print("Animal constructor")
        self.age = 1  # Every animal starts with age = 1

    def eat(self):
        # Method shared by all animals
        print("eat")


# Mammal inherits from Animal
class Mammal(Animal):

    # METHOD OVERRIDING:
    # The child class (Mammal) defines its own __init__
    # This replaces the parent's __init__ unless we explicitly call it with super().
    def __init__(self):
        print("Mammal constructor")
        # Mammal adds a new attribute that Animal does NOT have
        self.weight = 2

        # super().__init__() calls the parent (Animal) constructor
        # This is necessary if we want to keep 'age' or other Animal attributes.
        super().__init__()

    def walk(self):
        # Method specific to mammals
        print("walk")

    def walk(self):
        # New behavior specific to mammals
        print("walk")


# Another child class of Animal
# Fish also inherits:
# - age
# - eat()
class Fish(Animal):

    def swim(self):
        # Behavior specific to fish
        print("swim")


# Create an object of the Mammal class
m = Mammal()

# Because Mammal inherits from Animal, it can use the eat() method
m.eat()        # Calls the inherited method from Animal

# Mammal also inherits the age attribute from Animal
print(m.age)    # Prints 1 (inherited from Animal's __init__)
# The Object Class
# In Python, every class automatically inherits from the built-in "object" class.
# This means every class is ultimately a subclass of object.
# This is why we say: "Everything in Python is an object."

# Check if 'm' is an instance of Mammal
print(isinstance(m, Mammal))   # True → m was created from the Mammal class

# Check if 'm' is also an instance of Animal
# This is True because Mammal inherits from Animal
print(isinstance(m, Animal))   # True → Mammal is a subclass of Animal

# Check if 'm' is an instance of object
# Always True → all classes inherit from object
print(isinstance(m, object))   # True


# issubclass checks relationships between classes, not objects

# Is Mammal a subclass of Animal?
print(issubclass(Mammal, Animal))  # True

# Is Mammal a subclass of object?
# Yes → all classes in Python indirectly or directly inherit from object
print(issubclass(Mammal, object))  # True

# Is Animal a subclass of object?
print(issubclass(Animal, object))  # True

# Because super().__init__() was called, m has both attributes:
# - age   (from Animal)
# - weight (from Mammal)
print(m.age)     # Prints: 1
print(m.weight)  # Prints: 2

# Multi-level inheritance
# It exists in Python but is usually NOT recommended beyond 1 or 2 levels.
# Too many inheritance layers make the code hard to understand and maintain.
# Example:
# Animal -> Bird -> Chicken -> AnotherClass -> AnotherClass ...
# The deeper it goes, the easier it is to create bugs and “shoot yourself in the foot”.

# Bird inherits from Animal (level 1 inheritance)


class Bird(Animal):
    def fly(self):
        print("fly")  # Behavior added for birds


# Chicken inherits from Bird (level 2 inheritance)
# This means:
# - Chicken inherits from Bird
# - Bird inherits from Animal
# - So Chicken also indirectly inherits from Animal
class Chicken(Bird):
    pass  # No additional behavior for now, but it still inherits everything


# Multiple Inheritance
# A class can inherit from more than one parent class.
# This gives the child class access to all attributes and methods of both parents.
# But it can also create conflicts when the parents have methods with the SAME NAME.

class Employees:
    def greet(self):
        # Greet method from Employees class
        print("Employees Greet")


class Person:
    def greet(self):
        # Greet method from Person class
        print("Person Greet")


# Manager inherits from BOTH Employees and Person
class Manager(Employees, Person):
    # No methods are defined here, so the class will use the inherited ones
    pass


# If we create a Manager object:
m = Manager()
m.greet()

# Because Employees is the FIRST parent class,
# Python will search for greet() in this order (MRO - Method Resolution Order):
# Manager → Employees → Person → object
# So the output will be:
# "Employees Greet"


# BUT if we write:
#
# class Manager(Person, Employees):
#     pass
#
# Then the MRO changes to:
# Manager → Person → Employees → object
#
# In that case, calling m.greet() would print:
# "Person Greet"


# Good Example of Inheritance with Abstract Base Classes


# Custom exception for invalid actions on a stream.

class InvalidOperationError(Exception):
    pass


class Stream(ABC):

    # Stream is now an ABSTRACT BASE CLASS (ABC).
    # This means:
    # - It defines a common interface for all derived classes.
    # - It can provide shared code (open, close).
    # - But it CANNOT be instantiated directly.

    def __init__(self):
        # Every stream starts in a closed state
        self.opened = False

    def open(self):

        # Opens the stream.
        # If the stream is already open, raise an error.
        # This logic is shared by all types of streams.

        if self.opened:
            raise InvalidOperationError("Stream is already opened.")
        self.opened = True

    def close(self):

        # Closes the stream.
        # If the stream is already closed, raise an error.
        # This logic is shared by all types of streams.

        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False

    @abstractmethod
    def read(self):

        # ABSTRACT METHOD:
        # - Child classes MUST implement this method.
        # - Stream provides no default implementation.
        # - This forces each subclass to define how it reads data.

        pass


class FileStream(Stream):

    # FileStream inherits open() and close() from Stream.
    # It MUST implement the abstract read() method.

    def read(self):
        print("Reading Data From A File")


class NetworkStream(Stream):

    # NetworkStream also inherits the shared behavior from Stream.
    # It must also implement read() in its own way.

    def read(self):
        print("Reading Data From A Network")


class MemoryStream(Stream):

    # Another concrete implementation of Stream.
    # This class describes how to read from a memory-based stream.

    def read(self):
        print("Reading Data From A MemoryStream")


# We CANNOT do this:
# s = Stream()
# Because Stream contains an abstract method (read), it is not instantiable.

# Instead, we instantiate one of the concrete subclasses:
stream = MemoryStream()

# We can now use the inherited open() method
stream.open()

# Polymorphism
# Poly = Many
# Morph = Form
# Polymorphism = "Many Forms"
#
# In OOP, polymorphism allows different objects to respond to the same method
# call in their own unique way.


class UIControl(ABC):

    # UIControl is an abstract base class.
    # It defines a common interface for all UI controls.
    # Every control must implement the draw() method.

    @abstractmethod
    def draw(self):

        # Abstract method:
        # Must be implemented by derived classes (TextBox, DropDownList, etc.).

        pass


class TextBox(UIControl):

    # TextBox is a specific type of UIControl.
    # It provides its own implementation of draw().

    def draw(self):
        print("TextBox")


class DropDownList(UIControl):

    # DropDownList is another UIControl.
    # It also implements draw() in its own way.

    def draw(self):
        print("DropDownList")


def draw(controls):

    # This function takes a list of UIControl objects.
    # Because of polymorphism, it doesn't care what type each object is.
    # It simply calls draw(), and each object behaves according to its class.

    for control in controls:
        control.draw()  # Polymorphism in action


# Creating instances of different UI controls
ddl = DropDownList()
textBox = TextBox()

# Passing them to the draw() function
# Each control will use its own version of draw()
draw([ddl, textBox])


# Duck Typing
# "If it walks like a duck and quacks like a duck, it's a duck."
#
# In Python, we don't care about the TYPE of an object.
# We care only about whether the object has the required BEHAVIOR (methods).


class DropDownList:
    def draw(self):
        # This class has a draw() method
        print("DropDownList")


class TextBox:
    def draw(self):
        # This class also has a draw() method
        print("TextBox")


def draw(controls):

    # This function works with ANY object that has a draw() method.
    # It does NOT check the type of the object.
    # This is DUCK TYPING.

    for control in controls:
        control.draw()


# Creating objects
ddl = DropDownList()
textBox = TextBox()

# Because both objects have a draw() method,
# they can be passed to the draw() function.
draw([ddl, textBox])


# Extending Built-in Types
#
# In Python, you can inherit from built-in types (str, list, dict, etc.)
# to add new behaviors or modify existing ones.


class Text(str):

    # Text extends the built-in 'str' type.
    # This means it behaves exactly like a normal string,
    # but we can add our own custom methods.

    def duplicate(self):
        # Returns the string repeated twice
        return self + self


class TrackabelList(list):

    # TrackabelList extends the built-in 'list' type.
    # We override the append() method to add extra behavior.

    def append(self, object):
        # Custom behavior: print a message before appending
        print("append called")

        # Call the original list.append() method using super()
        super().append(object)


# Creating an instance of TrackabelList
my_list = TrackabelList()

# This will call our overridden append() method
my_list.append("Python")

word = Text("Hi")
print(word.duplicate())  # HiHi


# Data Classes with namedtuple
# namedtuple creates a lightweight, immutable class with named fields
Point = namedtuple("Point", ["x", "y"])

# Create two points
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)

# Access attributes like a normal object
print(p1.x)  # Output: 1

# p1.x = 10  # ERROR: namedtuples are immutable, cannot modify fields

# To "change" a value, create a new Point object
p1 = Point(x=10, y=2)

# Compare two points by their values, not by identity
print(p1 == p2)  # Output: False, because p1=(10,2) and p2=(1,2)
