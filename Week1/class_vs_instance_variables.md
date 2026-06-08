# Class Variables vs Instance Variables

## What is a Class Variable?

A class variable belongs to the class and is shared by all objects.

Example:

```python
class Employee:

    company = "Google"
```

Here:

```python
company
```

is a class variable.

Only one copy exists in memory.

---

## What is an Instance Variable?

An instance variable belongs to an object.

Example:

```python
class Employee:

    def __init__(self, name):
        self.name = name
```

Here:

```python
self.name
```

is an instance variable.

Each object gets its own copy.

---

## Example

```python
class Employee:

    company = "Google"

    def __init__(self, name):
        self.name = name


emp1 = Employee("Monika")
emp2 = Employee("John")
```

Memory:

```text
Class Employee
--------------
company = Google


emp1
-----
name = Monika


emp2
-----
name = John
```

---

## Why Use Class Variables?

Suppose all employees belong to:

```text
Google
```

Storing:

```python
self.company = "Google"
```

inside every object wastes memory.

Instead:

```python
company = "Google"
```

stores only one shared copy.

---

## Accessing Variables

### Accessing Class Variable

Using Class:

```python
Employee.company
```

Using Object:

```python
emp1.company
```

Both work.

---

### Accessing Instance Variable

Using Object:

```python
emp1.name
```

---

## Example

```python
class Employee:

    company = "Google"

    def __init__(self, name):
        self.name = name


emp1 = Employee("Monika")

print(emp1.company)
print(emp1.name)
```

Output:

```text
Google
Monika
```

---

## Modifying a Class Variable

```python
class Employee:

    company = "Google"
```

Change:

```python
Employee.company = "Microsoft"
```

Now:

```python
print(Employee.company)
```

Output:

```text
Microsoft
```

All objects see the updated value.

---

## Example

```python
emp1 = Employee("Monika")
emp2 = Employee("John")

Employee.company = "Microsoft"

print(emp1.company)
print(emp2.company)
```

Output:

```text
Microsoft
Microsoft
```

Reason:

Class variable is shared.

---

## Modifying an Instance Variable

```python
emp1.name = "Priya"
```

Now:

```python
print(emp1.name)
print(emp2.name)
```

Output:

```text
Priya
John
```

Reason:

Each object has its own copy.

---

# Important Edge Case 1

## Object Creates Its Own Variable

```python
class Employee:

    company = "Google"


emp1 = Employee()

emp1.company = "Amazon"
```

Many people think:

```text
Employee.company becomes Amazon
```

Wrong.

Python creates a new instance variable.

Memory:

```text
Employee
--------
company = Google


emp1
----
company = Amazon
```

---

## Output

```python
print(emp1.company)
print(Employee.company)
```

Output:

```text
Amazon
Google
```

---

# Important Edge Case 2

```python
class Employee:

    company = "Google"


emp1 = Employee()
emp2 = Employee()

emp1.company = "Amazon"

print(emp1.company)
print(emp2.company)
print(Employee.company)
```

Output:

```text
Amazon
Google
Google
```

Reason:

emp1 now has its own company variable.

---

# Variable Shadowing

This is an interview favorite.

```python
emp1.company = "Amazon"
```

creates:

```python
company
```

inside emp1.

This hides (shadows):

```python
Employee.company
```

for that object.

---

# Understanding __dict__

Object Variables:

```python
class Employee:

    company = "Google"

    def __init__(self, name):
        self.name = name


emp1 = Employee("Monika")
```

Check:

```python
print(emp1.__dict__)
```

Output:

```python
{
    'name': 'Monika'
}
```

Notice:

```text
company not present
```

because company belongs to the class.

---

## After Shadowing

```python
emp1.company = "Amazon"

print(emp1.__dict__)
```

Output:

```python
{
    'name': 'Monika',
    'company': 'Amazon'
}
```

Now company exists inside the object.

---

## Class Dictionary

```python
print(Employee.__dict__['company'])
```

Output:

```text
Google
```

Class variables are stored inside:

```python
Employee.__dict__
```

---

# Internal Lookup Mechanism

When Python executes:

```python
emp1.company
```

Search Order:

```text
1. Search inside emp1
2. Search inside Employee class
```

This is called Attribute Lookup.

---

## Example

```python
emp1.company = "Amazon"

print(emp1.company)
```

Python finds:

```text
emp1.company
```

first.

So:

```text
Amazon
```

is printed.

---

# Difference Table

| Class Variable | Instance Variable |
|---------------|------------------|
| Belongs to Class | Belongs to Object |
| One Shared Copy | Separate Copy Per Object |
| Stored in Class | Stored in Object |
| Memory Efficient | Object Specific |
| Accessed via Class or Object | Accessed via Object |
| Shared Data | Unique Data |

---

# Interview Questions

## What is a Class Variable?

A variable that belongs to the class and is shared by all objects.

---

## What is an Instance Variable?

A variable that belongs to an individual object.

---

## Where are Class Variables Stored?

Inside:

```python
ClassName.__dict__
```

---

## Where are Instance Variables Stored?

Inside:

```python
object.__dict__
```

---

## What Happens When We Do?

```python
emp1.company = "Amazon"
```

Python creates a new instance variable inside emp1.

It does not modify the class variable.

---

## What is Variable Shadowing?

When an instance variable hides a class variable with the same name.

---

# Revision Summary

## Class Variable

```python
company = "Google"
```

- Shared by all objects
- One copy
- Stored in class

---

## Instance Variable

```python
self.name = name
```

- Separate copy per object
- Stored in object

---

## Lookup Rule

```python
emp.variable
```

Python searches:

```text
Object → Class
```

---

## Writing Rule

```python
emp.variable = value
```

Creates or updates an instance variable.

---

## Writing Rule

```python
ClassName.variable = value
```

Updates the class variable.
