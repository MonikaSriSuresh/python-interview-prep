# Dependency Inversion Principle (DIP)

## Definition

Depend on abstractions.

Not on concrete implementations.

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

## Revision

Depend On Interfaces

Not Concrete Classes