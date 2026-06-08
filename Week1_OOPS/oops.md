# OOP Notes - Day 1

## What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects that contain both data and behavior.

### Benefits of OOP

* Code Reusability
* Maintainability
* Scalability
* Better Code Organization
* Real-world Modeling

---

## What is a Programming Paradigm?

A programming paradigm is a style or approach to programming that provides a way of organizing and structuring code to solve problems.

### Common Programming Paradigms

* Procedural Programming
* Object-Oriented Programming (OOP)
* Functional Programming

OOP is a programming paradigm that organizes code into classes and objects.

---

## Class

A class is a blueprint or template used to create objects.

A class defines:

* Attributes (Data)
* Methods (Behavior)

### Example

```python
class Employee:
    pass
```

### Interview Definition

A class is a user-defined blueprint that defines the attributes and methods that objects created from the class will have.

---

## Object

An object is an instance of a class created at runtime.

### Example

```python
emp = Employee()
```

Here, `emp` is an object.

### Interview Definition

An object is a runtime instance of a class that occupies memory and contains actual values for the attributes defined in the class.

---

## Constructor (**init**)

A constructor is a special method that is automatically called when an object is created.

### Purpose

* Initialize object attributes

### Example

```python
class Employee:

    def __init__(self, name):
        self.name = name
```

### Usage

```python
emp = Employee("Monika")
```

Python automatically calls:

```python
Employee.__init__(emp, "Monika")
```

---

## self Keyword

`self` refers to the current object.

### Purpose

* Access instance variables
* Access instance methods
* Store data inside the object

### Example

```python
class Employee:

    def __init__(self, name):
        self.name = name
```

Without `self`:

```python
name = name
```

The value is not stored inside the object.

With `self`:

```python
self.name = name
```

The value is stored inside the object.

### Interview Definition

`self` is a reference to the current object and is used to access and modify instance variables and methods belonging to that object.

---

## Instance Variables

Instance variables belong to an object.

### Example

```python
self.name
self.salary
```

### Characteristics

* Stored inside the object
* Each object gets its own copy
* Accessible throughout the object's lifetime

### Example

```python
emp1 = Employee("Monika")
emp2 = Employee("John")
```

Memory Representation:

```text
emp1.name = "Monika"
emp2.name = "John"
```

Changing `emp1.name` does not affect `emp2.name`.

---

## Local Variables

Local variables are created inside methods.

### Example

```python
def display(self):
    department = "IT"
```

### Characteristics

* Exist only while the method executes
* Not stored inside the object
* Destroyed after method execution

### Example

```python
emp.department
```

Results in:

```python
AttributeError
```

because `department` is a local variable.

---

## Instance Variable vs Local Variable

### Instance Variable

```python
self.name
```

* Belongs to the object
* Stored in object memory
* Exists as long as the object exists

### Local Variable

```python
department
```

* Belongs to the method
* Exists only during method execution
* Destroyed after method execution

---

## Object State

Each object maintains its own state.

### Example

```python
class Employee:

    def __init__(self, name):
        self.name = name

emp1 = Employee("Monika")
emp2 = Employee("John")

emp1.name = "Priya"
```

Output:

```python
print(emp1.name)
```

```text
Priya
```

```python
print(emp2.name)
```

```text
John
```

### Reason

Each object has its own copy of instance variables.

Changing one object's data does not affect another object's data.

---

## Encapsulation

Encapsulation is the process of bundling data and methods together and restricting direct access to internal data.

### Purpose

* Protect data
* Control access
* Prevent invalid modifications

### Example

```python
class BankAccount:

    def __init__(self):
        self.__balance = 50000
```

Private Variable:

```python
self.__balance
```

Access through methods:

```python
deposit()
withdraw()
get_balance()
```

### Interview Definition

Encapsulation is an OOP principle that combines data and methods into a single unit and restricts direct access to internal data, providing controlled access through methods.

---

# Quick Revision

## Class

Blueprint used to create objects.

## Object

Runtime instance of a class.

## Constructor

Special method automatically called when an object is created.

## self

Reference to the current object.

## Instance Variable

Variable that belongs to an object.

## Local Variable

Variable that exists only inside a method.

## Object State

Each object maintains its own copy of instance variables.

## Encapsulation

Protecting data by restricting direct access and providing controlled access through methods.


## Characteristics of an Object

Every object has three characteristics:

### State

The current values of the object's instance variables.

Example:

```python
emp = Employee("Monika", 100000)

### Interview Answer
What are the characteristics of an object?

An object has three characteristics:

State – represented by instance variables and their current values.
Behavior – represented by methods that define the actions the object can perform.
Identity – a unique memory location that distinguishes one object from another.