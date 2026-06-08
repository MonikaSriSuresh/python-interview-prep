# Encapsulation Notes

## What is Encapsulation?

Encapsulation is the process of bundling data and methods together into a single unit and restricting direct access to internal data.

### Purpose

- Protect Data
- Control Access
- Prevent Invalid Updates
- Improve Maintainability

---

## Real World Example

Bank Account

A user should not directly modify the account balance.

Instead of:

```python
account.balance = -10000
```

we provide methods:

```python
deposit()
withdraw()
get_balance()
```

---

## Private Variables

In Python, private variables are declared using double underscores.

Example:

```python
self.__balance
```

Example:

```python
class BankAccount:

    def __init__(self):
        self.__balance = 50000
```

Direct access:

```python
account.__balance
```

Results in:

```text
AttributeError
```

---

## Controlled Access

Access private data through methods.

Example:

```python
def deposit(self, amount):
    self.__balance += amount
```

```python
def get_balance(self):
    return self.__balance
```

---

## Advantages

- Data Security
- Data Validation
- Reduced Coupling
- Better Maintainability

---

## Interview Definition

Encapsulation is an OOP principle that combines data and methods into a single unit and restricts direct access to internal data by providing controlled access through methods.