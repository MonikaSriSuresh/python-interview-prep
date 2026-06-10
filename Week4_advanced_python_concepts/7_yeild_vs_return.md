# 07_Yield_vs_Return.md

# yield vs return in Python

## Why This Topic Matters

Generators work because of `yield`.

Understanding the difference between:

return

and

yield

is one of the most common Python interview questions.

---

# return

## Definition

return sends a value back to the caller and immediately terminates the function.

Example

def test():

```
print("A")

return 10

print("B")
```

Output

A

10

Notice:

```python
print("B")
```

never executes.

Function has already terminated.

---

# Execution Flow of return

Function Starts
↓
Code Executes
↓
return
↓
Function Ends
↓
State Destroyed

---

# Example

def add(a, b):

```
return a + b
```

result = add(10, 20)

Output

30

After return:

All local variables are destroyed.

---

# yield

## Definition

yield produces a value and pauses the function.

Unlike return, the function does not terminate.

Example

def test():

```
print("A")

yield 10

print("B")

yield 20
```

---

# Execution Flow

g = test()

Nothing executes yet.

Generator object is created.

---

First next()

next(g)

Output

A
10

Generator pauses.

---

Second next()

next(g)

Output

B
20

Generator pauses again.

---

Third next()

next(g)

Output

StopIteration

No more yields remain.

---

# Execution Flow of yield

Function Starts
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
↓
next()
↓
Resume

---

# State Preservation

This is the most important difference.

Example

def counter():

```
x = 1

yield x

x += 1

yield x
```

First next()

Output

1

Generator pauses.

x remains:

1

Second next()

Generator resumes.

x becomes:

2

Output

2

State is remembered.

---

# return vs yield Table

| return                   | yield              |
| ------------------------ | ------------------ |
| Terminates function      | Pauses function    |
| Returns final value      | Produces value     |
| State destroyed          | State preserved    |
| One result               | Multiple results   |
| Used in normal functions | Used in generators |
| Cannot resume            | Can resume         |

---

# Memory Comparison

Normal Function

def get_numbers():

```
return [1,2,3]
```

Creates all values immediately.

---

Generator

def get_numbers():

```
yield 1
yield 2
yield 3
```

Creates values only when needed.

Memory efficient.

---

# Example

return

def test():

```
return 1
```

Output

1

Function ends.

---

yield

def test():

```
yield 1
```

Output

Generator Object

Need:

next()

to get value.

---

# Why Generators Use yield

Because generators need:

Pause
Resume
State Preservation

return cannot provide these features.

yield can.

---

# Common Mistakes

Mistake 1

Thinking yield behaves exactly like return.

Wrong.

yield pauses.

return terminates.

---

Mistake 2

Thinking generator executes immediately.

Wrong.

Generator starts only when:

next()

is called.

---

Mistake 3

Thinking variables are destroyed after yield.

Wrong.

Variables remain alive.

---

# Interview Questions

Q1

Difference between yield and return?

return terminates the function.

yield pauses the function and preserves state.

---

Q2

Why is yield memory efficient?

Because values are generated only when needed.

---

Q3

Can a function contain multiple yields?

Yes.

That is exactly how generators produce multiple values.

---

Q4

Why do generators remember state?

Because execution pauses instead of terminating.

---

Q5

What does a generator function return?

A generator object.

---

# Key Takeaways

✓ return terminates

✓ yield pauses

✓ return destroys state

✓ yield preserves state

✓ yield enables generators

✓ generators are memory efficient

✓ next() resumes execution
