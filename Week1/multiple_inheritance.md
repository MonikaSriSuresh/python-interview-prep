# Multiple Inheritance and MRO

## What is Multiple Inheritance?

A class inheriting from more than one parent class.

Example:

```python
class Father:
    pass


class Mother:
    pass


class Child(Father, Mother):
    pass
```

---

## Why Use Multiple Inheritance?

Reuse functionality from multiple classes.

Example:

```text
DocumentProcessor
+
Logging
+
Audit
```

---

# Example

```python
class Father:

    def house(self):
        print("House")


class Mother:

    def jewelry(self):
        print("Jewelry")


class Child(Father, Mother):
    pass
```

Usage:

```python
child.house()
child.jewelry()
```

Output:

```text
House
Jewelry
```

---

# What is MRO?

MRO = Method Resolution Order

It determines the order in which Python searches for methods and attributes.

---

## Example

```python
class A:

    def show(self):
        print("A")


class B:

    def show(self):
        print("B")


class C(A, B):
    pass
```

Usage:

```python
obj = C()

obj.show()
```

Output:

```text
A
```

---

## Why?

MRO:

```text
C → A → B → object
```

Python finds:

```python
A.show()
```

first.

---

# Checking MRO

Method 1

```python
print(C.mro())
```

Method 2

```python
print(C.__mro__)
```

---

# Diamond Problem

Structure:

```text
      A
     / \
    B   C
     \ /
      D
```

Code:

```python
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass
```

---

## MRO

```python
print(D.mro())
```

Output:

```text
[D, B, C, A, object]
```

Python uses:

```text
C3 Linearization Algorithm
```

to calculate this order.

---

# Understanding super()

Most Important Interview Question.

Many people think:

```text
super() calls parent class
```

Partially Correct.

Actual Answer:

```text
super() calls the NEXT class in the MRO
```

---

# Example

```python
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
```

Output:

```text
C
B
A
```

---

# Example with Multiple Inheritance

```python
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
```

---

## MRO

```text
D → B → C → A → object
```

---

## Output

```text
D
B
C
A
```

---

# Why?

Execution Flow:

```text
D.show()
↓
B.show()
↓
C.show()
↓
A.show()
```

Each:

```python
super()
```

moves to the next class in MRO.

---

# Interview Question 1

```python
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
```

Output:

```text
A
```

Reason:

```text
C → A → B → object
```

---

# Interview Question 2

```python
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
```

Output:

```text
B
```

Reason:

Python finds:

```python
B.show()
```

first.

MRO:

```text
D → B → C → A → object
```

---

# Common Interview Questions

## What is Multiple Inheritance?

A class inheriting from multiple parent classes.

---

## What is MRO?

Method Resolution Order.

The order in which Python searches for methods and attributes.

---

## How to Check MRO?

```python
ClassName.mro()
```

or

```python
ClassName.__mro__
```

---

## What does super() do?

Correct Answer:

```text
Calls the next class in MRO
```

Not simply:

```text
Calls parent class
```

---

## Why is MRO Needed?

To resolve ambiguity when multiple parent classes contain methods with the same name.

---

# Revision Summary

## Multiple Inheritance

```python
class Child(Father, Mother)
```

Child inherits from multiple parents.

---

## MRO

Search order used by Python.

```text
Child → Parent1 → Parent2 → object
```

---

## Diamond Problem

```text
      A
     / \
    B   C
     \ /
      D
```

Resolved using:

```text
C3 Linearization
```

---

## super()

Important:

```text
super() = Next Class In MRO
```

Not:

```text
super() = Parent Class
```