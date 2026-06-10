"""
Single Responsibility Principle
"""


class Employee:

    def calculate_salary(self):
        print("Calculating Salary")


class EmployeeRepository:

    def save(self):
        print("Saving Employee")


class EmployeeReport:

    def generate(self):
        print("Generating Report")


employee = Employee()

employee.calculate_salary()

repo = EmployeeRepository()

repo.save()

report = EmployeeReport()

report.generate()