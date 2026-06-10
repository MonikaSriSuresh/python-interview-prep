# 02_Closures.md

# Closures in Python

## Definition

A closure is a function that remembers variables from its enclosing scope even after the enclosing function has finished execution.

In simple words:

A closure allows an inner function to access variables of the outer function even after the outer function has returned.

---

# Why Do We Need Closures?

Normally local variables disappear when a function ends.

Example:

```python
def test():
    x = 10

test()
```

After test() finishes:

```text
x is destroyed
```

Now consider:

```python
def outer():

    x = 10

    def inner():
        print(x)

    return inner
```

Question:

When outer() finishes, x should disappear.

Then how does inner() still print x?

Answer:

Python stores x inside a closure.

---

# Basic Example

```python
def outer():

    x = 10

    def inner():
        print(x)

    return inner

func = outer()

func()
```

Output:

```text
10
```

---

# Execution Flow

Step 1

```python
func = outer()
```

Creates:

```python
x = 10
```

Creates:

```python
inner()
```

Returns:

```python
inner
```

Function object.

---

Step 2

Python notices:

```python
inner()
```

uses:

```python
x
```

from outer scope.

Therefore Python preserves:

```python
x = 10
```

inside a closure.

---

Step 3

```python
func()
```

executes:

```python
inner()
```

which prints:

```text
10
```

---

# Memory Diagram

```text
func
 ↓
inner function
 ↓
Closure
 ↓
x = 10
```

Even though:

```python
outer()
```

has already finished.

---

# Important Point

Closure remembers variables.

Not function calls.

Not outputs.

Not return values.

Only referenced variables.

---

# Example 2

```python
def outer():

    name = "Monika"

    def inner():
        print(name)

    return inner

func = outer()

func()
```

Output

```text
Monika
```

Closure stores:

```text
name = Monika
```

---

# Example 3 - Multiple Variables

```python
def outer():

    x = 10
    y = 20

    def inner():
        print(x + y)

    return inner

func = outer()

func()
```

Output

```text
30
```

Closure stores:

```text
x = 10
y = 20
```

---

# Real Interview Example

```python
def multiplier(n):

    def multiply(x):
        return x * n

    return multiply

double = multiplier(2)

print(double(5))
```

Output

```text
10
```

---

# Why?

When:

```python
double = multiplier(2)
```

runs:

Closure stores:

```text
n = 2
```

Memory:

```text
double
 ↓
multiply
 ↓
Closure
 ↓
n = 2
```

Later:

```python
double(5)
```

becomes:

```python
5 * 2
```

Output:

```text
10
```

---

# Another Example

```python
triple = multiplier(3)

print(triple(5))
```

Output

```text
15
```

Memory:

```text
triple
 ↓
multiply
 ↓
Closure
 ↓
n = 3
```

Notice:

Different closures store different values.

---

# Closures vs Normal Functions

Normal Function

```python
def add(a, b):
    return a + b
```

No variables preserved.

After execution:

Everything is destroyed.

---

Closure

```python
def outer():

    x = 10

    def inner():
        print(x)

    return inner
```

Variable survives.

---

# Why Closures Matter

Closures are used in:

* Decorators
* Callbacks
* Event Handlers
* Flask Routes
* FastAPI Routes
* Function Factories

---

# Closures and Decorators

Decorator:

```python
def decorator(func):

    def wrapper():
        func()

    return wrapper
```

Closure stores:

```text
func
```

Even after:

```python
decorator()
```

finishes.

This is exactly why decorators work.

---

# Common Mistakes

Mistake 1

Thinking closure stores output.

Wrong.

Closure stores variables.

---

Mistake 2

Thinking closure stores function calls.

Wrong.

Closure stores references to variables.

---

Mistake 3

Thinking outer function is still running.

Wrong.

Outer function already finished.

Only variables are preserved.

---

# Interview Questions

## Q1

What is a closure?

Answer:

A closure is a function that remembers variables from its enclosing scope even after the enclosing function has returned.

---

## Q2

Why doesn't x disappear?

Because Python preserves referenced variables inside the closure.

---

## Q3

What is stored inside a closure?

Referenced variables from the outer scope.

---

## Q4

Why are closures important?

Decorators depend on closures.

---

## Q5

Can different closures store different values?

Yes.

Example:

```python
double = multiplier(2)

triple = multiplier(3)
```

Each closure stores its own value.

---

# Key Takeaways

✓ Closure remembers outer variables

✓ Outer function may finish

✓ Variables remain alive

✓ Foundation for decorators

✓ Used heavily in real-world Python

✓ Different closure instances can store different values
