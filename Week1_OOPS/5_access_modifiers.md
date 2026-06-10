# Access Modifiers in Python

---

# What are Access Modifiers?

Access modifiers control how class attributes and methods are accessed.

Unlike Java or C++, Python does not enforce access control strictly.

Python uses:

```text
Naming Conventions
```

Types:

1. Public
2. Protected
3. Private

---

# 1. Public Members

## Definition

Accessible from anywhere.

Syntax:

```python
self.name
```

Example:

```python
class Employee:

    def __init__(self):
        self.name = "Monika"
```

Usage:

```python
emp = Employee()

print(emp.name)
```

Output:

```text
Monika
```

---

## Characteristics

- Accessible Everywhere
- Default Access Level
- No Restrictions

---

# 2. Protected Members

## Definition

Intended for internal use and subclasses.

Syntax:

```python
self._salary
```

Single underscore.

Example:

```python
class Employee:

    def __init__(self):
        self._salary = 100000
```

Usage:

```python
print(emp._salary)
```

Output:

```text
100000
```

---

## Important

Protected members are accessible.

Python does not prevent access.

The underscore acts as a warning:

```text
Internal Use Only
```

---

## Inheritance Example

```python
class Employee:

    def __init__(self):
        self._salary = 100000


class Developer(Employee):

    def show_salary(self):
        print(self._salary)
```

Output:

```text
100000
```

Protected members are intended to be used by child classes.

---

# 3. Private Members

## Definition

Used to hide implementation details.

Syntax:

```python
self.__salary
```

Double underscore.

Example:

```python
class Employee:

    def __init__(self):
        self.__salary = 100000
```

Attempt:

```python
print(emp.__salary)
```

Output:

```text
AttributeError
```

---

# Name Mangling

Python does not create true private variables.

Instead it performs:

```text
Name Mangling
```

Internally:

```python
self.__salary
```

becomes:

```python
self._Employee__salary
```

Pattern:

```text
_ClassName__VariableName
```

---

## Proof

```python
class Employee:

    def __init__(self):
        self.__salary = 100000


emp = Employee()

print(emp.__dict__)
```

Output:

```python
{
    '_Employee__salary': 100000
}
```

---

## Accessing Private Variable

Possible but not recommended:

```python
print(emp._Employee__salary)
```

Output:

```text
100000
```

---

# Does Python Have True Private Variables?

Answer:

```text
No
```

Python uses Name Mangling.

It only makes accidental access difficult.

---

# Public vs Protected vs Private

| Access Type | Syntax | Accessible |
|-------------|---------|------------|
| Public | name | Everywhere |
| Protected | _name | Convention Only |
| Private | __name | Through Name Mangling |

---

# Real World Example

```python
class BankAccount:

    def __init__(self):

        self.account_holder = "Monika"

        self._account_type = "Savings"

        self.__balance = 50000
```

Explanation:

```text
account_holder -> Public

_account_type -> Protected

__balance -> Private
```

---

# Interview Questions

## What are Access Modifiers?

Mechanisms used to control access to attributes and methods.

---

## What access modifiers exist in Python?

- Public
- Protected
- Private

---

## How is Protected implemented?

Using a single underscore.

```python
_salary
```

---

## How is Private implemented?

Using double underscore.

```python
__salary
```

---

## What is Name Mangling?

Python internally renames private attributes.

Example:

```python
__salary
```

becomes:

```python
_Employee__salary
```

---

## Does Python support true private variables?

No.

Python uses Name Mangling rather than strict access control.

---

# Revision Summary

Public
------
self.name

Accessible Everywhere

---

Protected
---------
self._salary

Single Underscore

Convention Only

Used by Child Classes

---

Private
--------
self.__salary

Double Underscore

Uses Name Mangling

Internally:

_Employee__salary

---

Interview Point
---------------

Python does not have true private variables.

It uses Name Mangling to avoid accidental access.