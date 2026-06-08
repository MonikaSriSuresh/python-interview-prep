# Property Decorators

## What is @property?

Converts a method into attribute-style access.

Example:

```python
@property
def salary(self):
    return self.__salary
```

Usage:

```python
emp.salary
```

Internally:

```python
salary()
```

---

# Why Use Property?

- Encapsulation
- Validation
- Read Only Attributes
- Computed Attributes

---

# Getter

```python
@property
def salary(self):
    return self.__salary
```

---

# Setter

```python
@salary.setter
def salary(self, value):

    if value <= 0:
        raise ValueError

    self.__salary = value
```

---

# Deleter

```python
@salary.deleter
def salary(self):
    del self.__salary
```

---

# Read Only Property

No setter defined.

```python
@property
def emp_id(self):
    return self.__emp_id
```

Attempting:

```python
emp.emp_id = 100
```

Raises:

```text
AttributeError
```

---

# Computed Property

```python
@property
def annual_salary(self):
    return self.basic * 12
```

---

# Interview Questions

## What is @property?

Converts a method into attribute access.

---

## Why use @property?

Validation + Encapsulation.

---

## Difference Between Getter and Property?

Getter:

```python
emp.get_salary()
```

Property:

```python
emp.salary
```

Property is more Pythonic.

---

# Revision Summary

@property
Getter

@name.setter
Setter

@name.deleter
Deleter

Benefits:
- Validation
- Encapsulation
- Read Only Access
- Computed Attributes