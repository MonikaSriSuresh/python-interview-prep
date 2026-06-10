# Singleton Pattern

## Definition

Singleton is a design pattern that ensures only one instance of a class exists throughout the application and provides a global access point to it.

---

## Problem

Creating multiple objects for resources such as:

* Database Connections
* Logger
* Cache Manager
* Configuration Manager

can waste memory and system resources.

Example:

```python
db1 = Database()
db2 = Database()
db3 = Database()
```

Three different objects are created.

---

## Solution

Create only one object and return the same object whenever the class is instantiated.

---

## Why **new**() and not **init**()?

Object creation flow:

```text
__new__()
    ↓
Object Created
    ↓
__init__()
    ↓
Object Initialized
```

Singleton must control object creation, therefore it overrides `__new__()`.

---

## Implementation

```python
class Logger:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance
```

---

## Benefits

* Saves Memory
* Prevents Duplicate Resources
* Centralized Access
* Consistent Shared State

---

## Drawbacks

* Global State
* Difficult Unit Testing
* Can create hidden dependencies

---

## Real-World Examples

* Database Connection
* Logger
* Configuration Manager
* Application Cache

---

## Interview Answer

Singleton ensures only one instance of a class exists throughout the application and provides a global access point to that instance.
