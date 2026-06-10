"""
01_Functions_As_Objects.py

Functions As Objects - Practice File
"""


# ==================================================
# Example 1 - Function Object
# ==================================================

def greet():
    print("Hello")


print("Example 1")

print(greet)

# Expected Output:
# <function greet at 0x...>


# ==================================================
# Example 2 - Assign Function To Variable
# ==================================================

x = greet

print("\nExample 2")

x()

# Expected Output:
# Hello


# ==================================================
# Example 3 - Multiple References
# ==================================================

a = greet
b = greet

print("\nExample 3")

a()
b()

# Expected Output:
# Hello
# Hello


# ==================================================
# Example 4 - Function As Argument
# ==================================================

def execute(func):
    func()


print("\nExample 4")

execute(greet)

# Expected Output:
# Hello


# ==================================================
# Example 5 - Another Function As Argument
# ==================================================

def welcome():
    print("Welcome")


print("\nExample 5")

execute(welcome)

# Expected Output:
# Welcome


# ==================================================
# Example 6 - Returning Function
# ==================================================

def outer():

    def inner():
        print("Inner Function Executed")

    return inner


print("\nExample 6")

func = outer()

func()

# Expected Output:
# Inner Function Executed


# ==================================================
# Example 7 - Function Stored In List
# ==================================================

def add():
    print("Add")


def update():
    print("Update")


def delete():
    print("Delete")


operations = [add, update, delete]

print("\nExample 7")

for operation in operations:
    operation()

# Expected Output:
# Add
# Update
# Delete


# ==================================================
# Example 8 - Function Stored In Dictionary
# ==================================================

actions = {
    "add": add,
    "update": update,
    "delete": delete
}

print("\nExample 8")

actions["add"]()
actions["delete"]()

# Expected Output:
# Add
# Delete


# ==================================================
# Example 9 - Function Factory
# ==================================================

def create_greeting():

    def say_hello():
        print("Hello From Returned Function")

    return say_hello


print("\nExample 9")

func = create_greeting()

func()

# Expected Output:
# Hello From Returned Function


# ==================================================
# Example 10 - Higher Order Function
# ==================================================

def calculator(operation, a, b):

    return operation(a, b)


def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b):
    return a * b


print("\nExample 10")

print(calculator(add_numbers, 10, 20))

print(calculator(multiply_numbers, 10, 20))

# Expected Output:
# 30
# 200


# ==================================================
# Interview Question 1
# ==================================================

def hello():
    print("Hello")


x = hello

print("\nInterview Question 1")

print(x == hello)

# Expected Output:
# True


# ==================================================
# Interview Question 2
# ==================================================

def display(func):
    print("Before")
    func()
    print("After")


print("\nInterview Question 2")

display(hello)

# Expected Output:
# Before
# Hello
# After


# ==================================================
# Memory Identity Example
# ==================================================

print("\nMemory Identity Example")

print(x is hello)

# Expected Output:
# True


"""
REVISION NOTES

Functions are First-Class Objects

A function can:

1. Be assigned to a variable

x = greet

2. Be passed as an argument

execute(greet)

3. Be returned from another function

return inner

4. Be stored in a list

operations = [add, update, delete]

5. Be stored in a dictionary

actions = {
    "add": add
}

Important Interview Point

greet
    ↓
Function Object

x = greet

Now both variables point to the same function object.

Difference:

greet
    -> Function Object

greet()
    -> Executes Function

Functions As Objects
        ↓
Passing Functions
        ↓
Returning Functions
        ↓
Closures
        ↓
Decorators
"""