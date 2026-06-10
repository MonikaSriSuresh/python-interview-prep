"""
04_Decorators_With_Arguments.py
"""


# ==================================================
# Example 1
# ==================================================

def repeat(times):

    def decorator(func):

        def wrapper():

            for _ in range(times):
                func()

        return wrapper

    return decorator


@repeat(3)
def greet():
    print("Hello")


print("Example 1")

greet()


# ==================================================
# Example 2
# ==================================================

def repeat(times):

    def decorator(func):

        def wrapper():

            print("Starting")

            for _ in range(times):
                func()

            print("Ending")

        return wrapper

    return decorator


@repeat(2)
def welcome():
    print("Welcome")


print("\nExample 2")

welcome()


# ==================================================
# Example 3
# ==================================================

def require_role(role):

    def decorator(func):

        def wrapper():

            print(f"Checking Role: {role}")

            func()

        return wrapper

    return decorator


@require_role("admin")
def delete_user():
    print("User Deleted")


print("\nExample 3")

delete_user()


# ==================================================
# Example 4
# ==================================================

def retry(attempts):

    def decorator(func):

        def wrapper():

            print(f"Retry Count = {attempts}")

            func()

        return wrapper

    return decorator


@retry(5)
def save_data():
    print("Saving Data")


print("\nExample 4")

save_data()


# ==================================================
# Example 5
# ==================================================

def prefix(text):

    def decorator(func):

        def wrapper():

            print(text)

            func()

        return wrapper

    return decorator


@prefix("INFO:")
def start():
    print("Application Started")


print("\nExample 5")

start()


"""
REVISION NOTES

Normal Decorator

decorator
wrapper

Decorator With Arguments

repeat
decorator
wrapper

Python Converts

@repeat(3)

to

greet = repeat(3)(greet)

Closure Stores

func
times
"""