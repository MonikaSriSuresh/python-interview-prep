"""
Method Overloading in Python

Python does NOT support traditional method overloading.

If multiple methods have the same name,
Python keeps only the latest definition.

Alternatives:
1. Default Arguments
2. *args
3. **kwargs
"""

# --------------------------------------------------
# Example 1: Traditional Overloading (Not Supported)
# --------------------------------------------------

print("Example 1: Traditional Overloading")

class Calculator:

    # This method gets overwritten
    def add(self, a, b):
        return a + b

    # Python keeps only this method
    def add(self, a, b, c):
        return a + b + c


calc = Calculator()

try:
    print(calc.add(10, 20))
except TypeError as e:
    print("Error:", e)

print()

# --------------------------------------------------
# Example 2: Default Arguments
# --------------------------------------------------

print("Example 2: Default Arguments")

class CalculatorDefault:

    def add(self, a, b, c=0):
        return a + b + c


calc = CalculatorDefault()

print(calc.add(10, 20))
print(calc.add(10, 20, 30))

print()

# --------------------------------------------------
# Example 3: *args
# --------------------------------------------------

print("Example 3: *args")

class CalculatorArgs:

    def add(self, *args):
        return sum(args)


calc = CalculatorArgs()

print(calc.add(10))
print(calc.add(10, 20))
print(calc.add(10, 20, 30))
print(calc.add(10, 20, 30, 40))

print()

# --------------------------------------------------
# Example 4: Understanding *args
# --------------------------------------------------

print("Example 4: Understanding *args")

def show_args(*args):

    print("Args:", args)
    print("Type:", type(args))


show_args(1, 2, 3)

print()

# --------------------------------------------------
# Example 5: **kwargs
# --------------------------------------------------

print("Example 5: **kwargs")

def display(**kwargs):

    print(kwargs)

    for key, value in kwargs.items():
        print(key, "=", value)


display(name="Monika", age=30)

print()

# --------------------------------------------------
# Example 6: *args and **kwargs Together
# --------------------------------------------------

print("Example 6: *args and **kwargs")

def employee_info(*args, **kwargs):

    print("Args:", args)
    print("Kwargs:", kwargs)


employee_info(
    "Python",
    "AWS",
    name="Monika",
    experience=10
)