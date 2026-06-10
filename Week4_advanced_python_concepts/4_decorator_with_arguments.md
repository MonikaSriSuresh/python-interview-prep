# 04_Decorators_With_Arguments.md

# Decorators With Arguments

## Definition

A decorator with arguments is a decorator that accepts parameters before decorating a function.

Example:

@repeat(3)

Unlike normal decorators:

@decorator

---

# Why Do We Need Them?

Normal decorator:

@logger

Cannot customize behavior.

Decorator with arguments:

@retry(5)

@require_role("admin")

@cache(60)

Allows configuration.

---

# Internal Conversion

Python converts:

@repeat(3)
def greet():
print("Hello")

into:

greet = repeat(3)(greet)

---

# Why Three Functions?

Normal Decorator

Needs:

decorator
wrapper

Decorator With Arguments

Needs:

repeat
decorator
wrapper

---

# Structure

def repeat(times):

```
def decorator(func):

    def wrapper():

        for i in range(times):
            func()

    return wrapper

return decorator
```

---

# Flow

Step 1

repeat(3)

stores:

times = 3

returns:

decorator

Step 2

decorator(greet)

stores:

func = greet

returns:

wrapper

Step 3

greet now points to:

wrapper

Step 4

greet()

executes:

wrapper()

---

# Memory Diagram

greet
↓
wrapper
↓
closure
├── func = greet
└── times = 3

---

# Example

@repeat(3)
def greet():
print("Hello")

greet()

Output:

Hello
Hello
Hello

---

# Real World Example

Authentication

@require_role("admin")

Rate Limiting

@rate_limit(100)

Retry Logic

@retry(5)

Caching

@cache(60)

---

# Why Closures Matter

Wrapper remembers:

func

and

times

Even after:

repeat()

and

decorator()

finish execution.

---

# Common Mistakes

Mistake 1

Thinking repeat() is the decorator.

Wrong.

repeat() returns the decorator.

Mistake 2

Thinking wrapper stores only func.

Wrong.

Wrapper stores:

func
times

Mistake 3

Confusing:

@decorator

with

@decorator()

They are different.

---

# Interview Questions

Q1

Why do decorator arguments require three functions?

Because:

1. Outer function receives decorator arguments.
2. Middle function receives decorated function.
3. Wrapper executes additional logic.

---

Q2

Python converts:

@repeat(3)

into?

Answer:

greet = repeat(3)(greet)

---

Q3

What does closure store?

func

times

---

# Key Takeaways

✓ Decorator arguments require three functions

✓ Python uses:

repeat(3)(greet)

✓ Wrapper remembers:

func
times

✓ Used in authentication, retries and caching
