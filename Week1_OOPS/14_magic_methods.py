"""
Magic Methods / Dunder Methods
"""

# --------------------------------------------------
# Example 1 : __str__
# --------------------------------------------------

class Employee:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Employee Name: {self.name}"


emp = Employee("Monika")

print("Example 1")
print(emp)

print()

# --------------------------------------------------
# Example 2 : __repr__
# --------------------------------------------------

class Employee:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Employee('{self.name}')"


emp = Employee("Monika")

print("Example 2")
print(repr(emp))

print()

# --------------------------------------------------
# Example 3 : __str__ + __repr__
# --------------------------------------------------

class Employee:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Employee Name: {self.name}"

    def __repr__(self):
        return f"Employee('{self.name}')"


emp = Employee("Monika")

print("Example 3")
print(emp)
print(repr(emp))

print()

# --------------------------------------------------
# Example 4 : __len__
# --------------------------------------------------

class Team:

    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)


team = Team(["Monika", "John", "Priya"])

print("Example 4")
print(len(team))

print()

# --------------------------------------------------
# Example 5 : __eq__
# --------------------------------------------------

class Employee:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


emp1 = Employee("Monika")
emp2 = Employee("Monika")

print("Example 5")
print(emp1 == emp2)

print()

# --------------------------------------------------
# Example 6 : __lt__
# --------------------------------------------------

class Employee:

    def __init__(self, salary):
        self.salary = salary

    def __lt__(self, other):
        return self.salary < other.salary


emp1 = Employee(100000)
emp2 = Employee(200000)

print("Example 6")
print(emp1 < emp2)

print()

# --------------------------------------------------
# Example 7 : __add__
# --------------------------------------------------

class Employee:

    def __init__(self, salary):
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary


emp1 = Employee(100000)
emp2 = Employee(200000)

print("Example 7")
print(emp1 + emp2)

print()

# --------------------------------------------------
# Example 8 : Operator Overloading
# --------------------------------------------------

class Employee:

    def __init__(self, salary):
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary


emp1 = Employee(300000)
emp2 = Employee(100000)

print("Example 8")
print(emp1 + emp2)
print(emp1 - emp2)