"""
Operator Overloading in Python
"""

# --------------------------------------------------
# Example 1 : Without Operator Overloading
# --------------------------------------------------

class Employee:

    def __init__(self, salary):
        self.salary = salary


emp1 = Employee(100000)
emp2 = Employee(200000)

try:
    print(emp1 + emp2)
except TypeError as e:
    print("Error:", e)

print()

# --------------------------------------------------
# Example 2 : Overloading +
# --------------------------------------------------

class Employee:

    def __init__(self, salary):
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary


emp1 = Employee(100000)
emp2 = Employee(200000)

print("Addition:")
print(emp1 + emp2)

print()

# --------------------------------------------------
# Example 3 : Overloading -
# --------------------------------------------------

class Employee:

    def __init__(self, salary):
        self.salary = salary

    def __sub__(self, other):
        return self.salary - other.salary


emp1 = Employee(300000)
emp2 = Employee(100000)

print("Subtraction:")
print(emp1 - emp2)

print()

# --------------------------------------------------
# Example 4 : Overloading >
# --------------------------------------------------

class Employee:

    def __init__(self, salary):
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary


emp1 = Employee(300000)
emp2 = Employee(100000)

print("Greater Than:")
print(emp1 > emp2)

print()

# --------------------------------------------------
# Example 5 : Overloading <
# --------------------------------------------------

class Employee:

    def __init__(self, salary):
        self.salary = salary

    def __lt__(self, other):
        return self.salary < other.salary


emp1 = Employee(100000)
emp2 = Employee(300000)

print("Less Than:")
print(emp1 < emp2)

print()

# --------------------------------------------------
# Example 6 : Overloading ==
# --------------------------------------------------

class Employee:

    def __init__(self, emp_id):
        self.emp_id = emp_id

    def __eq__(self, other):
        return self.emp_id == other.emp_id


emp1 = Employee(101)
emp2 = Employee(101)

print("Equality:")
print(emp1 == emp2)

print()

# --------------------------------------------------
# Example 7 : Multiple Operators
# --------------------------------------------------

class Employee:

    def __init__(self, salary):
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary


emp1 = Employee(500000)
emp2 = Employee(200000)

print("Multiple Operators")
print("Addition:", emp1 + emp2)
print("Subtraction:", emp1 - emp2)
print("Greater:", emp1 > emp2)
print("Less:", emp1 < emp2)