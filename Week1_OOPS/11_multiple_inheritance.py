"""
Multiple Inheritance and MRO
"""

# --------------------------------------------------
# Example 1: Basic Multiple Inheritance
# --------------------------------------------------

print("Example 1: Basic Multiple Inheritance")


class Father:

    def house(self):
        print("Father House")


class Mother:

    def jewelry(self):
        print("Mother Jewelry")


class Child(Father, Mother):
    pass


child = Child()

child.house()
child.jewelry()

print()

# --------------------------------------------------
# Example 2: Method Conflict
# --------------------------------------------------

print("Example 2: Method Conflict")


class Father:

    def show(self):
        print("Father")


class Mother:

    def show(self):
        print("Mother")


class Child(Father, Mother):
    pass


child = Child()

child.show()

print("MRO:", Child.mro())

print()

# --------------------------------------------------
# Example 3: MRO Demonstration
# --------------------------------------------------

print("Example 3: MRO")


class A:

    def show(self):
        print("A")


class B:

    def show(self):
        print("B")


class C(A, B):
    pass


obj = C()

obj.show()

print("MRO:", C.mro())

print()

# --------------------------------------------------
# Example 4: Diamond Problem
# --------------------------------------------------

print("Example 4: Diamond Problem")


class A:

    def show(self):
        print("A")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


obj = D()

obj.show()

print("MRO:", D.mro())

print()

# --------------------------------------------------
# Example 5: super() with Single Inheritance
# --------------------------------------------------

print("Example 5: super()")


class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        print("B")
        super().show()


class C(B):

    def show(self):
        print("C")
        super().show()


obj = C()

obj.show()

print()

# --------------------------------------------------
# Example 6: super() with Multiple Inheritance
# --------------------------------------------------

print("Example 6: super() + MRO")


class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        print("B")
        super().show()


class C(A):

    def show(self):
        print("C")
        super().show()


class D(B, C):

    def show(self):
        print("D")
        super().show()


obj = D()

obj.show()

print("MRO:", D.mro())

print()

# --------------------------------------------------
# Example 7: Interview Question
# --------------------------------------------------

print("Example 7: Interview Question")


class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        print("B")


class C(A):

    def show(self):
        print("C")


class D(B, C):
    pass


obj = D()

obj.show()

print("MRO:", D.mro())