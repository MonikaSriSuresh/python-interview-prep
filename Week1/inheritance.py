"""
Inheritance
Method Overriding
super()
Polymorphism
"""

class Employee:

    def __init__(self, name):
        self.name = name

    def work(self):
        print("Employee Working")


class Developer(Employee):

    def __init__(self, name, language):

        super().__init__(name)

        self.language = language

    def work(self):
        print("Writing Code")

        super().work()

    def code(self):
        print(f"{self.name} writes {self.language}")


dev = Developer("Monika", "Python")

dev.work()

print()

dev.code()