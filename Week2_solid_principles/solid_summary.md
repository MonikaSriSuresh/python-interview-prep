# SOLID Principles

SOLID is a set of 5 design principles used to create maintainable, scalable and flexible software.

---

# S - Single Responsibility Principle (SRP)

## Definition

A class should have only one reason to change.

## Meaning

One Class = One Responsibility

## Bad Example

```python
class Employee:

    def calculate_salary(self):
        pass

    def save_to_db(self):
        pass
```

Multiple responsibilities.

SRP Violation.

## Good Example

```python
class Employee:
    pass


class EmployeeRepository:
    pass
```

Separate responsibilities.

## Interview Answer

A class should have only one responsibility and therefore one reason to change.

---

# O - Open Closed Principle (OCP)

## Definition

Open For Extension
Closed For Modification

## Meaning

Add new functionality without changing existing code.

## Bad Example

```python
if payment_type == "UPI":
    pass

elif payment_type == "CARD":
    pass
```

Need to modify code for new payment types.

OCP Violation.

## Good Example

```python
class Payment(ABC):
    pass


class UPIPayment(Payment):
    pass


class CardPayment(Payment):
    pass
```

Add new classes instead of modifying old code.

## Interview Answer

Software entities should be open for extension but closed for modification.

---

# L - Liskov Substitution Principle (LSP)

## Definition

Child class should replace parent class without breaking behavior.

## Bad Example

```python
class Bird:

    def fly(self):
        pass


class Penguin(Bird):

    def fly(self):
        raise Exception()
```

Penguin cannot behave like Bird.

LSP Violation.

## Interview Answer

Objects of a subclass should be replaceable with objects of the parent class without affecting correctness.

---

# I - Interface Segregation Principle (ISP)

## Definition

Do not force classes to implement methods they do not need.

## Bad Example

```python
class Worker:

    def work(self):
        pass

    def eat(self):
        pass
```

Robot forced to implement eat().

ISP Violation.

## Good Example

```python
class Workable:
    pass


class Eatable:
    pass
```

Split interfaces.

## Interview Answer

Large interfaces should be divided into smaller and specific interfaces.

---

# D - Dependency Inversion Principle (DIP)

## Definition

Depend on abstractions, not concrete implementations.

## Bad Example

```python
class UserService:

    def __init__(self):
        self.db = MySQLDatabase()
```

Tightly coupled.

DIP Violation.

## Good Example

```python
class UserService:

    def __init__(self, db):
        self.db = db
```

Dependency injected from outside.

## Interview Answer

High-level modules should depend on abstractions rather than concrete implementations.

---

# Quick Revision

SRP
----
One Class = One Responsibility

OCP
----
Open For Extension
Closed For Modification

LSP
----
Child Should Replace Parent
Without Breaking Behavior

ISP
----
Do Not Force Classes To Implement
Methods They Don't Need

DIP
----
Depend On Abstractions
Not Concrete Classes