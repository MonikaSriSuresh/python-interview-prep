# Single Responsibility Principle (SRP)

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

    def generate_report(self):
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

class EmployeeReport:
    pass
```

## Interview Answer

A class should have only one responsibility and one reason to change.

## Revision

One Class
=
One Responsibility