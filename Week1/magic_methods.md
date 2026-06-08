# Magic Methods (Dunder Methods)

## What are Magic Methods?

Magic methods are special methods that start and end with double underscores.

Example:

```python
__init__
__str__
__repr__
__len__
__eq__
```

Also called:

```text
Dunder Methods
(Double Underscore Methods)
```

---

# Why Do We Need Them?

Magic methods allow custom objects to behave like built-in Python objects.

Example:

```python
len(my_list)
```

Internally:

```python
my_list.__len__()
```

Example:

```python
print(emp)
```

Internally:

```python
emp.__str__()
```

---

# Object Lifecycle

```python
emp = Employee("Monika")
```

Python Internally:

```python
obj = Employee.__new__(Employee)
Employee.__init__(obj, "Monika")
```

Flow:

```text
__new__()
↓
__init__()
↓
Object Ready
```

---

# __init__()

## Purpose

Initialize object state.

Example:

```python
class Employee:

    def __init__(self, name):
        self.name = name
```

Usage:

```python
emp = Employee("Monika")
```

---

# __str__()

## Purpose

User friendly string representation.

Example:

```python
class Employee:

    def __str__(self):
        return "Employee Object"
```

Usage:

```python
print(emp)
```

Output:

```text
Employee Object
```

---

## Without __str__()

Output:

```text
<__main__.Employee object at 0x1234>
```

Not useful.

---

# __repr__()

## Purpose

Developer representation.

Example:

```python
class Employee:

    def __repr__(self):
        return "Employee('Monika')"
```

Usage:

```python
repr(emp)
```

Output:

```python
Employee('Monika')
```

---

# __str__ vs __repr__

| __str__ | __repr__ |
|----------|----------|
| User Friendly | Developer Friendly |
| print(obj) | repr(obj) |
| Readable | Unambiguous |

---

# Interview Question

What happens if __str__ is missing?

Python falls back to:

```python
__repr__()
```

---

# __len__()

## Purpose

Supports:

```python
len(obj)
```

Example:

```python
class Team:

    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)
```

Usage:

```python
team = Team(["A", "B", "C"])
print(len(team))
```

Output:

```text
3
```

---

# __eq__()

## Purpose

Controls:

```python
obj1 == obj2
```

Without __eq__:

```python
emp1 == emp2
```

compares memory addresses.

---

Example:

```python
class Employee:

    def __eq__(self, other):
        return self.name == other.name
```

Usage:

```python
emp1 = Employee("Monika")
emp2 = Employee("Monika")

print(emp1 == emp2)
```

Output:

```text
True
```

---

# __lt__()

Less Than Operator

```python
<
```

Example:

```python
def __lt__(self, other):
    return self.salary < other.salary
```

Usage:

```python
emp1 < emp2
```

---

# __gt__()

Greater Than Operator

```python
>
```

Example:

```python
def __gt__(self, other):
    return self.salary > other.salary
```

---

# Operator Overloading

## What is Operator Overloading?

Giving operators custom behavior.

Example:

```python
+
==
>
<
```

---

# __add__()

Example:

```python
class Employee:

    def __init__(self, salary):
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary
```

Usage:

```python
emp1 + emp2
```

Output:

```text
300000
```

---

# Internal Working

Python:

```python
emp1 + emp2
```

Internally:

```python
emp1.__add__(emp2)
```

---

# __sub__()

Supports:

```python
emp1 - emp2
```

Internally:

```python
emp1.__sub__(emp2)
```

---

# __mul__()

Supports:

```python
*
```

Internally:

```python
__mul__()
```

---

# Common Dunder Methods

| Method | Purpose |
|----------|----------|
| __init__ | Constructor |
| __str__ | User String |
| __repr__ | Developer String |
| __len__ | len(obj) |
| __eq__ | == |
| __lt__ | < |
| __gt__ | > |
| __add__ | + |
| __sub__ | - |
| __mul__ | * |

---

# Interview Questions

## What are Magic Methods?

Special methods automatically invoked by Python.

---

## Why are they called Dunder Methods?

Double underscore methods.

---

## Difference Between __str__ and __repr__?

__str__:

```text
Readable for Users
```

__repr__:

```text
Readable for Developers
```

---

## How does len(obj) work?

Python calls:

```python
obj.__len__()
```

---

## How does obj1 == obj2 work?

Python calls:

```python
obj1.__eq__(obj2)
```

---

## What is Operator Overloading?

Giving custom behavior to operators using magic methods.

---

# Revision Summary

__init__
Initialize Object

__str__
print(obj)

__repr__
repr(obj)

__len__
len(obj)

__eq__
==

__lt__
<

__gt__
>

__add__
+

Magic Methods allow custom objects to behave like built-in Python objects.