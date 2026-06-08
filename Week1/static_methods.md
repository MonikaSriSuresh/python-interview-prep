# Static Methods in Python

## What is a Static Method?

A static method is a method that:

- Does not use self
- Does not use cls
- Works like a normal function
- Is placed inside a class for logical grouping

Defined using:

```python
@staticmethod
```

---

## Why Do We Need Static Methods?

Suppose we need a utility function.

```python
def is_adult(age):
    return age >= 18
```

This function:

- Does not need object data
- Does not need class data

But logically belongs to Employee.

---

## Syntax

```python
class Employee:

    @staticmethod
    def is_adult(age):
        return age >= 18
```

Usage:

```python
print(Employee.is_adult(20))
```

Output:

```text
True
```

---

## Example 1

```python
class Employee:

    @staticmethod
    def greet():
        print("Welcome")
```

Usage:

```python
Employee.greet()
```

Output:

```text
Welcome
```

---

## Example 2

```python
class DocumentProcessor:

    @staticmethod
    def is_pdf(filename):
        return filename.endswith(".pdf")
```

Usage:

```python
print(DocumentProcessor.is_pdf("invoice.pdf"))
```

Output:

```text
True
```

---

## Internal Working

```python
Employee.greet()
```

Python simply executes:

```python
greet()
```

No self.

No cls.

---

## Edge Case 1

```python
class Employee:

    @staticmethod
    def greet():
        print("Welcome")


emp = Employee()

emp.greet()
```

Output:

```text
Welcome
```

Works.

But no object data is used.

---

## Edge Case 2

This is wrong:

```python
class Employee:

    @staticmethod
    def display():
        print(self.name)
```

Output:

```text
NameError
```

Reason:

Static methods don't receive self.

---

## Instance Method vs Class Method vs Static Method

| Feature | Instance Method | Class Method | Static Method |
|----------|----------|----------|----------|
| Decorator | None | @classmethod | @staticmethod |
| First Parameter | self | cls | None |
| Access Instance Variables | Yes | No | No |
| Access Class Variables | Yes | Yes | No |
| Use Case | Object Behavior | Class Operations | Utility Functions |

---

## When to Use

### Instance Method

When working with:

```python
self.name
self.salary
```

---

### Class Method

When working with:

```python
cls.company
```

---

### Static Method

When working with:

```python
age
filename
email
mobile
```

Utility operations.

---

## Interview Questions

### What is a Static Method?

A method that belongs to a class but does not require access to either instance data or class data.

---

### What decorator is used?

```python
@staticmethod
```

---

### Does a static method receive self?

No.

---

### Does a static method receive cls?

No.

---

## Memory Trick

Think:

### Instance Method

Needs object?

```text
YES → self
```

### Class Method

Needs class?

```text
YES → cls
```

### Static Method

Needs neither?

```text
YES → staticmethod
```

---

## Revision Summary

- Uses @staticmethod
- No self
- No cls
- Utility/helper methods
- Can be called using class or object
- Does not access object or class state
