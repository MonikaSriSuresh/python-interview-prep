# Method Overloading in Python

## What is Method Overloading?

Method overloading means creating multiple methods with the same name but different parameters.

Example (Java):

```java
add(int a, int b)

add(int a, int b, int c)

add(double a, double b)
```

Same method name.

Different parameter lists.

---

## Does Python Support Method Overloading?

No.

Python does NOT support traditional method overloading.

---

## Why?

Python identifies methods only by their name.

If multiple methods have the same name:

```python
class Calculator:

    def add(self, a, b):
        pass

    def add(self, a, b, c):
        pass
```

Python keeps only:

```python
def add(self, a, b, c):
    pass
```

The previous method is overwritten.

---

## Example

```python
class Calculator:

    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c
```

Usage:

```python
calc.add(10, 20)
```

Output:

```text
TypeError
```

Reason:

Python only sees:

```python
add(self, a, b, c)
```

---

# How Python Achieves Overloading

Python uses:

1. Default Arguments
2. *args
3. **kwargs

---

# Method 1: Default Arguments

```python
class Calculator:

    def add(self, a, b, c=0):
        return a + b + c
```

Usage:

```python
calc.add(10, 20)
```

Output:

```text
30
```

Usage:

```python
calc.add(10, 20, 30)
```

Output:

```text
60
```

---

# Method 2: *args

## What is *args?

Allows a function to accept any number of positional arguments.

Python stores them inside a tuple.

Example:

```python
def show(*args):
    print(args)
```

Usage:

```python
show(1, 2, 3)
```

Output:

```python
(1, 2, 3)
```

---

## Datatype of args

```python
tuple
```

Example:

```python
print(type(args))
```

Output:

```python
<class 'tuple'>
```

---

## Example

```python
class Calculator:

    def add(self, *args):
        return sum(args)
```

Usage:

```python
calc.add(10)
```

Output:

```text
10
```

Usage:

```python
calc.add(10, 20)
```

Output:

```text
30
```

Usage:

```python
calc.add(10, 20, 30)
```

Output:

```text
60
```

---

# Method 3: **kwargs

## What is **kwargs?

Allows a function to accept any number of keyword arguments.

Python stores them inside a dictionary.

Example:

```python
def display(**kwargs):
    print(kwargs)
```

Usage:

```python
display(name="Monika", age=30)
```

Output:

```python
{
    'name': 'Monika',
    'age': 30
}
```

---

## Datatype of kwargs

```python
dict
```

---

## Example

```python
def display(**kwargs):

    for key, value in kwargs.items():
        print(key, value)
```

Output:

```text
name Monika
age 30
```

---

# *args vs **kwargs

| Feature | *args | **kwargs |
|----------|--------|----------|
| Accepts | Positional Arguments | Keyword Arguments |
| Datatype | Tuple | Dictionary |
| Symbol | * | ** |

---

# Common Interview Questions

## Does Python support method overloading?

No.

Python keeps only the latest method definition.

---

## How does Python achieve method overloading?

Using:

```text
Default Arguments
*args
**kwargs
```

---

## What is *args?

Accepts variable positional arguments.

Stored as:

```python
tuple
```

---

## What is **kwargs?

Accepts variable keyword arguments.

Stored as:

```python
dictionary
```

---

## Difference Between *args and **kwargs

### *args

```python
show(1, 2, 3)
```

Positional arguments.

Stored as tuple.

---

### **kwargs

```python
show(name="Monika")
```

Keyword arguments.

Stored as dictionary.

---

# Edge Case 1

```python
def test(*args):
    print(args)

test()
```

Output:

```python
()
```

Empty tuple.

---

# Edge Case 2

```python
def test(**kwargs):
    print(kwargs)

test()
```

Output:

```python
{}
```

Empty dictionary.

---

# Edge Case 3

```python
def test(*args, **kwargs):
    print(args)
    print(kwargs)
```

Usage:

```python
test(1, 2, name="Monika")
```

Output:

```python
(1, 2)

{
    'name': 'Monika'
}
```

---

# Revision Summary

## Method Overloading

Python does NOT support traditional overloading.

Reason:

Python keeps only the latest method definition.

---

## Alternatives

1. Default Arguments
2. *args
3. **kwargs

---

## *args

- Variable positional arguments
- Stored as Tuple

---

## **kwargs

- Variable keyword arguments
- Stored as Dictionary

---

## Interview One-Liner

Python does not support traditional method overloading. It achieves similar behavior using default arguments, *args, and **kwargs.


Method overloading is a type of compile-time polymorphism because the same method name can have multiple implementations based on different parameter lists. However, Python does not support traditional method overloading and instead uses default arguments, *args, and **kwargs to achieve similar behavior.