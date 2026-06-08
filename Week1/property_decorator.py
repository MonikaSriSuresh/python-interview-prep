"""
Property Decorators
"""


class Employee:

    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):

        if value <= 0:
            raise ValueError(
                "Salary must be positive"
            )

        self.__salary = value

    @salary.deleter
    def salary(self):
        print("Salary Deleted")
        del self.__salary


emp = Employee(100000)

print(emp.salary)

emp.salary = 200000

print(emp.salary)

# emp.salary = -1000

del emp.salary