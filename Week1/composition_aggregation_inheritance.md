# Composition vs Aggregation vs Inheritance

---

# Inheritance

## Definition

Inheritance allows a child class to acquire properties and methods from a parent class.

Relationship:

```text
IS-A
```

Example:

```python
class Employee:

    def work(self):
        print("Working")


class Developer(Employee):
    pass
```

Relationship:

```text
Developer IS-A Employee
```

---

## Real World Examples

```text
Dog IS-A Animal

Car IS-A Vehicle

Developer IS-A Employee
```

---

## Advantages

- Code Reuse
- Method Overriding
- Polymorphism

---

## Disadvantages

- Tight Coupling
- Wrong hierarchy can create design issues
- Difficult to modify large inheritance trees

---

# Composition

## Definition

Composition is a strong HAS-A relationship.

One class owns another class.

Relationship:

```text
HAS-A
```

---

## Example

```python
class Engine:

    def start(self):
        print("Engine Started")


class Car:

    def __init__(self):
        self.engine = Engine()
```

Relationship:

```text
Car HAS-A Engine
```

---

## Why Composition?

Engine belongs to Car.

Engine is created inside Car.

```python
self.engine = Engine()
```

---

## Lifecycle

```text
Destroy Car
↓
Destroy Engine
```

Engine lifecycle depends on Car.

---

## Real World Examples

```text
House HAS-A Room

Car HAS-A Engine

Computer HAS-A CPU

Mobile HAS-A Battery
```

---

## Advantages

- Loose Coupling
- Flexible Design
- Easy Maintenance
- Easy Testing
- Preferred over Inheritance

---

# Aggregation

## Definition

Aggregation is a weak HAS-A relationship.

One class uses another class but does not own it.

---

## Example

```python
class Address:

    def __init__(self, city):
        self.city = city


class Employee:

    def __init__(self, address):
        self.address = address
```

Usage:

```python
addr = Address("Chennai")

emp = Employee(addr)
```

Relationship:

```text
Employee HAS-A Address
```

---

## Why Aggregation?

Address is created outside Employee.

```python
addr = Address("Chennai")
```

and passed inside:

```python
Employee(addr)
```

---

## Lifecycle

```text
Destroy Employee
↓
Address Still Exists
```

Address lifecycle is independent.

---

## Real World Examples

```text
Department HAS-A Employee

School HAS-A Teacher

Team HAS-A Player
```

---

# Composition vs Aggregation

## Composition

Object created inside class.

Example:

```python
self.engine = Engine()
```

Lifecycle:

```text
Dependent
```

Strong HAS-A Relationship.

---

## Aggregation

Object created outside class.

Example:

```python
engine = Engine()

car = Car(engine)
```

Lifecycle:

```text
Independent
```

Weak HAS-A Relationship.

---

# Composition vs Inheritance

## Inheritance

```text
IS-A Relationship
```

Example:

```text
Developer IS-A Employee
```

---

## Composition

```text
HAS-A Relationship
```

Example:

```text
Car HAS-A Engine
```

---

# Why Composition is Preferred Over Inheritance?

Inheritance:

```python
class Car(Engine)
```

Means:

```text
Car IS-A Engine
```

Wrong Relationship.

---

Composition:

```python
class Car:

    def __init__(self):
        self.engine = Engine()
```

Means:

```text
Car HAS-A Engine
```

Correct Relationship.

---

Benefits:

- Loose Coupling
- Better Reusability
- Flexible Design
- Easier Maintenance

---

# Interview Questions

## What is Inheritance?

A child class acquiring properties and methods from a parent class.

Relationship:

```text
IS-A
```

---

## What is Composition?

One class owns another class.

Relationship:

```text
Strong HAS-A
```

Object created inside the class.

---

## What is Aggregation?

One class uses another class.

Relationship:

```text
Weak HAS-A
```

Object created outside the class.

---

## Difference Between Composition and Aggregation?

### Composition

```python
self.engine = Engine()
```

Created inside.

Lifecycle dependent.

---

### Aggregation

```python
engine = Engine()

car = Car(engine)
```

Created outside.

Lifecycle independent.

---

## Why is Composition Preferred?

Because it promotes:

- Loose Coupling
- Better Design
- Easier Maintenance

---

# Revision Summary

Inheritance
-----------
IS-A Relationship

Developer IS-A Employee

Pros:
- Code Reuse
- Polymorphism

Cons:
- Tight Coupling

---

Composition
-----------
Strong HAS-A Relationship

Car HAS-A Engine

Object created inside class.

Lifecycle dependent.

Preferred over Inheritance.

---

Aggregation
-----------
Weak HAS-A Relationship

Employee HAS-A Address

Object created outside class.

Lifecycle independent.

---

Memory Trick

Inheritance:
IS-A

Composition:
Creates Object Inside

Aggregation:
Receives Object From Outside    