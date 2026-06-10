"""
Liskov Substitution Principle
"""


class Bird:

    def fly(self):
        print("Flying")


class Sparrow(Bird):
    pass


bird = Sparrow()

bird.fly()