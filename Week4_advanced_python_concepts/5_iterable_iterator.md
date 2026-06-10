# 05_Iterable_Iterator.md

# Iterable vs Iterator

## Why This Topic Matters

When you write:

for x in nums:
print(x)

Python is secretly using:

iter()
next()

Understanding iterables and iterators helps understand:

* for loops
* generators
* yield
* memory-efficient programming

---

# What is an Iterable?

An iterable is an object that can produce an iterator.

Examples:

list
tuple
set
string
dictionary

Example:

nums = [1, 2, 3]

nums is iterable.

---

# Why Is It Called Iterable?

Because we can iterate over it.

Example:

for x in nums:
print(x)

Output:

1
2
3

---

# What is an Iterator?

An iterator is an object that remembers the current position while traversing a collection.

Created using:

iter()

Example:

nums = [1, 2, 3]

it = iter(nums)

---

# What Does iter() Do?

Converts an iterable into an iterator.

Example:

nums = [1, 2, 3]

it = iter(nums)

Memory:

nums
↓
[1,2,3]

it
↓
Iterator

---

# What Does next() Do?

Returns the next value from an iterator.

Example:

next(it)

Output:

1

Next call:

next(it)

Output:

2

Next call:

next(it)

Output:

3

---

# StopIteration

After all elements are exhausted:

next(it)

raises:

StopIteration

Example:

nums = [1]

it = iter(nums)

next(it)

next(it)

Output:

StopIteration

---

# Internal Working Of For Loop

Code:

for x in nums:
print(x)

Internally:

it = iter(nums)

while True:

```
try:

    x = next(it)

    print(x)

except StopIteration:

    break
```

---

# Memory Diagram

Iterable

nums
↓
[1,2,3]

Iterator

it
↓
Current Position

---

# Example

nums = [1,2,3]

it = iter(nums)

print(next(it))

print(next(it))

print(next(it))

Output:

1
2
3

---

# Iterator Remembers Position

nums = [1,2,3]

it = iter(nums)

print(next(it))

print(next(it))

Output:

1
2

Iterator remembers position.

---

# Multiple Iterators

nums = [1,2,3]

it1 = iter(nums)

it2 = iter(nums)

Each iterator has its own position.

Example:

next(it1)

Output:

1

next(it2)

Output:

1

next(it1)

Output:

2

---

# Iterable vs Iterator

| Iterable                 | Iterator            |
| ------------------------ | ------------------- |
| Collection               | Position Tracker    |
| Uses iter()              | Uses next()         |
| Cannot remember position | Remembers position  |
| Example: list            | Example: iter(list) |

---

# Interview Questions

Q1

What is an iterable?

An object that can produce an iterator.

---

Q2

What is an iterator?

An object that remembers current traversal position.

---

Q3

Difference between iterable and iterator?

Iterable = collection

Iterator = position tracker

---

Q4

How does a for loop work internally?

Using:

iter()

and

next()

with StopIteration.

---

# Key Takeaways

✓ Iterable is a collection

✓ Iterator tracks current position

✓ iter() creates iterator

✓ next() gets next value

✓ StopIteration ends iteration

✓ for loop uses iter() and next()
