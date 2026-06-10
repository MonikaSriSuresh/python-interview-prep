"""
OOP Fundamentals
Class
Object
Constructor
self
Instance Variables
"""

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")


emp1 = Employee("Monika", 100000)
emp2 = Employee("John", 120000)

emp1.display()

print()

emp2.display()