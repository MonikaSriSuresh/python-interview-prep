# 06_Generators.md

# Generators in Python

## Definition

A generator is a special type of iterator that generates values one at a time using the `yield` keyword.

Unlike lists, generators do not store all values in memory.

They produce values only when requested.

---

# Why Do We Need Generators?

Suppose:

```python
nums = [i for i in range(1000000)]
```

Python creates:

0
1
2
3
...
999999

and stores everything in memory.

This can consume significant memory.

Generator:

```python
nums = (i for i in range(1000000))
```

creates only:

Generator Object

Values are generated one by one.

---

# Creating a Generator

```python
def numbers():

    yield 1

    yield 2

    yield 3
```

---

# Generator Object

```python
g = numbers()
```

Output:

```text
<generator object ...>
```

The function does not execute immediately.

It returns a generator object.

---

# Execution Starts With next()

```python
next(g)
```

Output:

1

Execution pauses at:

```python
yield 1
```

---

# Second next()

```python
next(g)
```

Output:

2

Execution resumes after:

```python
yield 1
```

and pauses at:

```python
yield 2
```

---

# Third next()

```python
next(g)
```

Output:

3

---

# Fourth next()

```python
next(g)
```

Raises:

StopIteration

because there are no more yields.

---

# Generator Execution Flow

Generator Function
↓
Generator Object
↓
next()
↓
yield value
↓
Pause
↓
next()
↓
Resume
↓
yield value
↓
Pause

---

# Pause and Resume

This is the most important feature.

Example:

```python
def test():

    print("A")

    yield 1

    print("B")

    yield 2
```

Execution:

First next():

Output:

A
1

Generator pauses.

Second next():

Output:

B
2

Generator resumes.

---

# Memory Diagram

Generator

g
↓
Generator Object
↓
Current State
↓
Current Position

Generator remembers where it stopped.

---

# Generators Are Iterators

Example:

```python
g = numbers()
```

Supports:

```python
next(g)
```

Therefore:

Every Generator Is An Iterator

---

# But

Not Every Iterator Is A Generator

Example:

```python
nums = [1,2,3]

it = iter(nums)
```

Iterator?

Yes

Generator?

No

Because no yield exists.

---

# Generator Expression

List Comprehension

```python
[i for i in range(5)]
```

Output:

List

Generator Expression

```python
(i for i in range(5))
```

Output:

Generator Object

---

# Memory Comparison

List

```python
nums = [i for i in range(1000000)]
```

Creates all values.

High Memory Usage.

Generator

```python
nums = (i for i in range(1000000))
```

Creates values only when needed.

Low Memory Usage.

---

# Real World Usage

Reading Large Files

```python
for line in file:
```

Data Streaming

Log Processing

CSV Processing

API Data Streams

---

# Interview Questions

Q1

What is a generator?

A special iterator that generates values lazily using yield.

---

Q2

Why use generators?

To save memory.

---

Q3

Are generators iterators?

Yes.

---

Q4

Are all iterators generators?

No.

---

Q5

Difference between list comprehension and generator expression?

List stores everything.

Generator produces values on demand.

---

# Key Takeaways

✓ Generator uses yield

✓ Returns generator object

✓ Produces values lazily

✓ Saves memory

✓ Supports next()

✓ Generator is a special iterator

✓ Remembers execution state
