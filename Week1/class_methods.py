class Employee:

    company = "Google"

    def __init__(self, name):
        self.name = name

    @classmethod
    def show_company(cls):
        print(f"Company: {cls.company}")

    @classmethod
    def change_company(cls, company):
        cls.company = company

    @classmethod
    def from_string(cls, emp_string):
        name, company = emp_string.split("-")

        employee = cls(name)
        cls.company = company

        return employee


# Example 1: Accessing Class Variable
emp1 = Employee("Monika")
emp2 = Employee("John")

Employee.show_company()

# Example 2: Modifying Class Variable
Employee.change_company("Microsoft")

print("\nAfter changing company:")
print(emp1.company)
print(emp2.company)

# Example 3: Calling Class Method Using Object
emp1.change_company("Amazon")

print("\nAfter calling class method through object:")
print(Employee.company)
print(emp1.company)
print(emp2.company)

# Example 4: Alternative Constructor
emp3 = Employee.from_string("Priya-Adobe")

print("\nAlternative Constructor:")
print(emp3.name)
print(Employee.company)

# Example 5: Understanding cls
print("\nClass Information:")
print(Employee)