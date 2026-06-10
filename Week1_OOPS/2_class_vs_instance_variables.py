class Employee:

    company = "Google"  # Class Variable

    def __init__(self, name):
        self.name = name  # Instance Variable


# Creating Objects
emp1 = Employee("Monika")
emp2 = Employee("John")

print("Initial Values")
print(emp1.company)
print(emp2.company)
print(emp1.name)
print(emp2.name)

# Changing Class Variable
Employee.company = "Microsoft"

print("\nAfter Changing Class Variable")
print(emp1.company)
print(emp2.company)

# Changing Instance Variable
emp1.name = "Priya"

print("\nAfter Changing Instance Variable")
print(emp1.name)
print(emp2.name)

# Edge Case 1 - Shadowing
emp1.company = "Amazon"

print("\nShadowing Example")
print(emp1.company)
print(emp2.company)
print(Employee.company)

# __dict__ Example
print("\nObject Dictionary")
print(emp1.__dict__)

print("\nClass Dictionary Company")
print(Employee.__dict__["company"])

# Attribute Lookup
print("\nAttribute Lookup")
print(emp1.company)
print(emp2.company)