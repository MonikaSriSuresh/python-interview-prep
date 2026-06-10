# Class Methods in Python

## What is a Class Method?

A class method is a method that operates on the class itself rather than an object.

It is defined using:

```python
@classmethod
```

and receives:

```python
cls
```

as the first parameter.

---

## Why Do We Need Class Methods?

Class methods are used when working with:

- Class variables
- Class-level operations
- Alternative constructors

---

## Syntax

```python
class Employee:

    company = "Google"

    @classmethod
    def show_company(cls):
        print(cls.company)
```

---

## What is cls?

Just like:

```python
self
```

refers to the current object,

```python
cls
```

refers to the current class.

Example:

```python
class Employee:

    @classmethod
    def show_class(cls):
        print(cls)
```

Usage:

```python
Employee.show_class()
```

Output:

```text
<class '__main__.Employee'>
```

---

## Example 1: Modifying a Class Variable

```python
class Employee:

    company = "Google"

    @classmethod
    def change_company(cls, company):
        cls.company = company


print(Employee.company)

Employee.change_company("Microsoft")

print(Employee.company)
```

Output:

```text
Google
Microsoft
```

---

## Can We Call a Class Method Using an Object?

Yes.

```python
emp = Employee()

emp.change_company("Amazon")
```

Works.

Why?

Because Python automatically passes:

```python
cls = Employee
```

not:

```python
cls = emp
```

---

## Alternative Constructor

One of the most important interview questions.

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, emp_string):

        name, salary = emp_string.split("-")

        return cls(name, int(salary))
```

Usage:

```python
emp = Employee.from_string("Monika-100000")

print(emp.name)
print(emp.salary)
```

Output:

```text
Monika
100000
```

---

## Internal Working

Instance Method:

```python
emp.display()
```

Internally:

```python
Employee.display(emp)
```

self = emp

---

Class Method:

```python
Employee.show_company()
```

Internally:

```python
Employee.show_company(Employee)
```

cls = Employee

---

## Edge Case 1

```python
class Employee:

    company = "Google"

    @classmethod
    def change_company(cls, company):
        cls.company = company


emp = Employee()

emp.change_company("Microsoft")

print(Employee.company)
```

Output:

```text
Microsoft
```

Reason:

Class methods always work with the class.

---

## Edge Case 2

```python
class Employee:

    company = "Google"

    @classmethod
    def change_company(cls, company):
        cls.company = company


Employee.change_company("Microsoft")

emp = Employee()

print(emp.company)
```

Output:

```text
Microsoft
```

Reason:

New objects see the updated class variable.

---

## Interview Questions

### What is a Class Method?

A class method operates on the class itself rather than an instance.

---

### What decorator is used?

```python
@classmethod
```

---

### What does cls represent?

The current class.

---

### Difference Between self and cls

| self | cls |
|--------|--------|
| Current Object | Current Class |
| Instance Method | Class Method |
| Works with Instance Variables | Works with Class Variables |

---

## Revision Summary

- Uses @classmethod
- First parameter is cls
- cls refers to the class
- Used for class variables
- Used for alternative constructors
- Can be called using class or object
- Best practice: call using class
