"""
02_Closures.py

Closures Practice File
"""


# ==================================================
# Example 1 - Basic Closure
# ==================================================

def outer():

    x = 10

    def inner():
        print(x)

    return inner


print("Example 1")

func = outer()

func()


# ==================================================
# Example 2 - Closure with String
# ==================================================

def outer_name():

    name = "Monika"

    def inner():
        print(name)

    return inner


print("\nExample 2")

func = outer_name()

func()


# ==================================================
# Example 3 - Multiple Variables
# ==================================================

def outer_sum():

    x = 10
    y = 20

    def inner():
        print(x + y)

    return inner


print("\nExample 3")

func = outer_sum()

func()


# ==================================================
# Example 4 - Function Factory
# ==================================================

def multiplier(n):

    def multiply(x):
        return x * n

    return multiply


double = multiplier(2)

print("\nExample 4")

print(double(5))


# ==================================================
# Example 5 - Different Closures
# ==================================================

double = multiplier(2)

triple = multiplier(3)

print("\nExample 5")

print(double(5))
print(triple(5))


# ==================================================
# Example 6 - Closure Memory Concept
# ==================================================

def create_printer(message):

    def printer():
        print(message)

    return printer


hello = create_printer("Hello")

print("\nExample 6")

hello()


# ==================================================
# Example 7 - Power Function Factory
# ==================================================

def power(exponent):

    def calculate(number):
        return number ** exponent

    return calculate


square = power(2)

cube = power(3)

print("\nExample 7")

print(square(4))
print(cube(4))


# ==================================================
# Example 8 - Closure Used By Decorators
# ==================================================

def decorator(func):

    def wrapper():

        print("Before")

        func()

        print("After")

    return wrapper


def greet():
    print("Hello")


wrapped = decorator(greet)

print("\nExample 8")

wrapped()


# ==================================================
# Interview Question
# ==================================================

def outer_interview():

    x = 100

    def inner():
        print(x)

    return inner


func = outer_interview()

print("\nInterview Question")

func()


"""
REVISION NOTES

Closure =
Function + Remembered Variables

Example:

double = multiplier(2)

Memory:

double
  ↓
multiply
  ↓
closure
  ↓
n = 2

Important:

1. Outer function finishes execution.
2. Variables normally disappear.
3. Python preserves variables used by inner function.
4. Inner function can still access them.
5. Decorators depend on closures.
"""