# Inheritance Notes

## What is Inheritance?

Inheritance is an OOP principle where a child class acquires properties and methods from a parent class.

Benefits:

- Code Reusability
- Reduced Duplication
- Easier Maintenance
- Extensibility

---

## Parent Class

Also called:

- Base Class
- Super Class

Example:

```python
class Employee:
    pass
```

---

## Child Class

Also called:

- Derived Class
- Sub Class

Example:

```python
class Developer(Employee):
    pass
```

Developer inherits Employee.

---

## Method Lookup

When Python executes:

```python
dev.work()
```

It searches:

1. Child Class
2. Parent Class

If found in child class, it executes immediately.

If not found, it searches the parent class.

---

## Constructor Inheritance

Parent constructor is inherited by child classes.

Example:

```python
class Employee:

    def __init__(self, name):
        self.name = name


class Developer(Employee):
    pass
```

Usage:

```python
dev = Developer("Monika")
```

---

## super()

super() is used to access parent class methods and constructors.

Example:

```python
class Developer(Employee):

    def __init__(self, name, language):

        super().__init__(name)

        self.language = language #also anny additional parameter included in the chiled class
```

Equivalent to:

```python
Employee.__init__(self, name)
```

---

## Method Overriding

Method overriding occurs when a child class provides its own implementation of a parent class method.

Example:

```python
class Employee:

    def work(self):
        print("Employee Working")


class Developer(Employee):

    def work(self):
        print("Writing Code")
```

Output:

```python
dev = Developer()

dev.work()
```

Result:

```text
Writing Code
```

---

## Polymorphism

Polymorphism means one interface, many forms.

Example:

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")
```

Usage:

```python
animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

Output:

```text
Bark
Meow
```

Same method call.

Different behavior.

---

## Difference Between Concepts

### Inheritance

Code Reuse

### Method Overriding

Modify Parent Behavior

### Polymorphism

Same Method, Different Behavior

---

## Interview Definitions

### Inheritance

A child class acquires properties and methods from a parent class.

### Method Overriding

A child class provides its own implementation of a parent class method.

### Polymorphism

The same method call behaves differently depending on the object invoking it.

### super()

Used to access parent class methods and constructors from a child class.