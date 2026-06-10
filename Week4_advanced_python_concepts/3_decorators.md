# 03_Decorators.md

# Decorators in Python

## Definition

A decorator is a function that takes another function as input, adds extra functionality, and returns a new function without modifying the original function.

In simple words:

A decorator wraps a function and adds behavior before or after the original function executes.

---

# Why Do We Need Decorators?

Suppose we have:

```python
def login():
    print("Login")

def logout():
    print("Logout")

def dashboard():
    print("Dashboard")
```

Now imagine every function needs:

* Authentication
* Logging
* Timing
* Error handling

Without decorators:

```python
def login():
    print("Before")
    print("Login")
    print("After")
```

Same code gets repeated.

Decorators solve this problem.

---

# Basic Decorator

```python
def decorator(func):

    def wrapper():

        print("Before")

        func()

        print("After")

    return wrapper
```

---

# Manual Decoration

```python
def greet():
    print("Hello")

greet = decorator(greet)

greet()
```

Output:

Before
Hello
After

---

# Execution Flow

Step 1

```python
decorator(greet)
```

Receives:

```python
func = greet
```

Step 2

Creates:

```python
wrapper()
```

Step 3

Returns:

```python
wrapper
```

Step 4

```python
greet = wrapper
```

Now:

```text
greet
 ↓
wrapper
```

---

# Memory Diagram

```text
greet
 ↓
wrapper
 ↓
closure
 ↓
func = original greet
```

Wrapper remembers the original function through closure.

---

# Decorator Syntax

Instead of:

```python
greet = decorator(greet)
```

Python provides:

```python
@decorator
def greet():
    print("Hello")
```

Python internally converts:

```python
@decorator
def greet():
    print("Hello")
```

to:

```python
def greet():
    print("Hello")

greet = decorator(greet)
```

Exactly the same.

---

# Example

```python
@decorator
def greet():
    print("Hello")

greet()
```

Output:

Before
Hello
After

---

# Why Closures Are Needed

Decorator:

```python
def decorator(func):

    def wrapper():
        func()

    return wrapper
```

After:

```python
return wrapper
```

decorator() finishes.

Yet:

```python
func()
```

still works.

Why?

Closure remembers:

```text
func = original function
```

---

# Real World Example - Logging

```python
def logger(func):

    def wrapper():

        print("Starting Function")

        func()

        print("Ending Function")

    return wrapper
```

---

# Real World Example - Authentication

```python
def auth(func):

    def wrapper():

        print("Checking Authentication")

        func()

    return wrapper
```

---

# Decorator Flow

Functions As Objects
↓
Passing Functions
↓
Returning Functions
↓
Closures
↓
Decorators

---

# Common Mistakes

Mistake 1

Thinking decorator executes immediately.

Wrong.

Decorator returns wrapper.

Wrapper executes later.

---

Mistake 2

Thinking original function is lost.

Wrong.

Wrapper remembers it through closure.

---

Mistake 3

Thinking @ creates new functionality.

Wrong.

It is only syntactic sugar.

---

# Interview Questions

## Q1

What is a decorator?

A function that wraps another function and adds behavior without modifying the original function.

---

## Q2

How does @decorator work?

Python converts:

```python
@decorator
def greet():
```

to:

```python
greet = decorator(greet)
```

---

## Q3

Why do decorators require closures?

Because wrapper must remember the original function after decorator() finishes execution.

---

## Q4

What is stored inside the decorator closure?

```text
func = original function
```

---

# Key Takeaways

✓ Decorators wrap functions

✓ Avoid duplicate code

✓ Depend on closures

✓ Use higher-order functions

✓ @ is syntactic sugar

✓ Used heavily in real-world Python
