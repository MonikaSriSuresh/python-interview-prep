# Operator Overloading in Python

## What is Operator Overloading?

Operator Overloading means giving operators custom behavior for user-defined classes.

Example:

```python
10 + 20
```

Python knows how to add integers.

But for:

```python
emp1 + emp2
```

Python doesn't know what to do unless we define it.

---

# Why Do We Need It?

Allows custom objects to behave like built-in objects.

Example:

```python
emp1 + emp2
```

could mean:

```text
Add Salaries
```

---

# Internal Working

When Python sees:

```python
emp1 + emp2
```

Internally:

```python
emp1.__add__(emp2)
```

---

# Overloading +

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

---

# Overloading -

```python
def __sub__(self, other):
    return self.salary - other.salary
```

Usage:

```python
emp1 - emp2
```

Internally:

```python
emp1.__sub__(emp2)
```

---

# Overloading *

```python
def __mul__(self, other):
    return self.salary * other.salary
```

Usage:

```python
emp1 * emp2
```

---

# Overloading /

```python
def __truediv__(self, other):
    return self.salary / other.salary
```

Usage:

```python
emp1 / emp2
```

---

# Overloading ==

```python
def __eq__(self, other):
    return self.emp_id == other.emp_id
```

Usage:

```python
emp1 == emp2
```

---

# Overloading >

```python
def __gt__(self, other):
    return self.salary > other.salary
```

Usage:

```python
emp1 > emp2
```

---

# Overloading <

```python
def __lt__(self, other):
    return self.salary < other.salary
```

Usage:

```python
emp1 < emp2
```

---

# Common Operator Methods

| Operator | Magic Method |
|-----------|-------------|
| + | __add__ |
| - | __sub__ |
| * | __mul__ |
| / | __truediv__ |
| == | __eq__ |
| > | __gt__ |
| < | __lt__ |
| >= | __ge__ |
| <= | __le__ |

---

# Interview Questions

## What is Operator Overloading?

Giving operators custom behavior for custom classes.

---

## Why is it needed?

To make custom objects behave like built-in objects.

---

## What happens internally?

```python
emp1 + emp2
```

becomes:

```python
emp1.__add__(emp2)
```

---

## Is Operator Overloading a type of Polymorphism?

Yes.

Reason:

```text
One Operator
Many Behaviors
```

Examples:

10 + 20       -> Addition

"Hi" + "All"  -> Concatenation

emp1 + emp2   -> Salary Addition

---

# Revision Summary

Operator Overloading

Purpose:
Custom behavior for operators.

Examples:

+  -> __add__()

-  -> __sub__()

*  -> __mul__()

/  -> __truediv__()

== -> __eq__()

>  -> __gt__()

<  -> __lt__()

Internal Working:

emp1 + emp2

=

emp1.__add__(emp2)

Interview Point:

Operator Overloading is a form of Polymorphism.