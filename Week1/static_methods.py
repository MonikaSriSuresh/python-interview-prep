class Employee:

    company = "Google"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def greet():
        print("Welcome")

    @staticmethod
    def is_adult(age):
        return age >= 18

    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email


# Example 1
Employee.greet()

# Example 2
print("\nAge Validation:")
print(Employee.is_adult(20))
print(Employee.is_adult(15))

# Example 3
print("\nEmail Validation:")
print(Employee.is_valid_email("monika@gmail.com"))
print(Employee.is_valid_email("monika"))

# Example 4: Calling Static Method Using Object
emp = Employee("Monika")

print("\nCalling Static Method Using Object:")
emp.greet()

# Example 5
print("\nUtility Function Examples:")
print(Employee.is_adult(30))
print(Employee.is_valid_email("test@yahoo.com"))