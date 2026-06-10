"""
03_Decorators.py

Decorators Practice File
"""


# ==================================================
# Example 1 - Manual Decoration
# ==================================================

def decorator(func):

    def wrapper():

        print("Before")

        func()

        print("After")

    return wrapper


def greet():
    print("Hello")


print("Example 1")

greet = decorator(greet)

greet()


# ==================================================
# Example 2 - @ Syntax
# ==================================================

def decorator(func):

    def wrapper():

        print("Before")

        func()

        print("After")

    return wrapper


@decorator
def welcome():
    print("Welcome")


print("\nExample 2")

welcome()


# ==================================================
# Example 3 - Logging Decorator
# ==================================================

def logger(func):

    def wrapper():

        print("Starting Function")

        func()

        print("Ending Function")

    return wrapper


@logger
def process_file():
    print("Processing File")


print("\nExample 3")

process_file()


# ==================================================
# Example 4 - Authentication Decorator
# ==================================================

def auth(func):

    def wrapper():

        print("Checking Authentication")

        func()

    return wrapper


@auth
def dashboard():
    print("Dashboard Opened")


print("\nExample 4")

dashboard()


# ==================================================
# Example 5 - Multiple Decorated Functions
# ==================================================

@logger
def login():
    print("Login")


@logger
def logout():
    print("Logout")


print("\nExample 5")

login()
logout()


# ==================================================
# Example 6 - Memory Concept
# ==================================================

def simple_decorator(func):

    def wrapper():
        func()

    return wrapper


def hello():
    print("Hello")


wrapped = simple_decorator(hello)

print("\nExample 6")

wrapped()


# ==================================================
# Interview Question 1
# ==================================================

def interview_decorator(func):

    def wrapper():

        print("Before")

        func()

        print("After")

    return wrapper


@interview_decorator
def test():
    print("Test")


print("\nInterview Question 1")

test()


# ==================================================
# Interview Question 2
# ==================================================

def uppercase(func):

    def wrapper():

        result = func()

        print(result.upper())

    return wrapper


@uppercase
def message():
    return "hello world"


print("\nInterview Question 2")

message()


"""
REVISION NOTES

Decorator

decorator(func)
    ↓
wrapper
    ↓
return wrapper

Manual Decoration

greet = decorator(greet)

Decorator Syntax

@decorator

becomes

greet = decorator(greet)

Memory

greet
 ↓
wrapper
 ↓
closure
 ↓
func = original greet

Decorator depends on:

Functions As Objects
    ↓
Closures
    ↓
Decorator
"""