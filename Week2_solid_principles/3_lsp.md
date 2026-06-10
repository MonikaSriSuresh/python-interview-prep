# Liskov Substitution Principle (LSP)

---

# Definition

A child class should be able to replace its parent class
without breaking the correctness of the program.

In simple words:

Child Must Behave Like Parent

---

# Bad Design

```python
class Bird:

    def fly(self):
        print("Flying")


class Penguin(Bird):

    def fly(self):
        raise Exception("Cannot Fly")
```

Usage:

```python
bird = Penguin()

bird.fly()
```

Output:

```text
Exception
```

---

# Why Is This Wrong?

Parent Class Promise:

```text
Every Bird can fly
```

Child Class:

```text
Penguin cannot fly
```

When Penguin replaces Bird:

```text
Program breaks
```

LSP Violation.

---

# Solution

Separate Flying Birds from Non-Flying Birds.

```python
class Bird:
    pass


class FlyingBird(Bird):

    def fly(self):
        print("Flying")


class Sparrow(FlyingBird):
    pass


class Penguin(Bird):
    pass
```

Now:

```text
Penguin is not forced to fly
```

LSP Followed.

---

# Benefits

- Correct inheritance hierarchy
- No unexpected runtime errors
- Better design
- Better maintainability

---

# Interview Questions

Q. What is LSP?

A. Child classes should replace parent classes without breaking behavior.

---

Q. Why is Penguin-Bird an LSP violation?

A. Bird promises fly(), but Penguin cannot fly.

---

# Quick Revision

Parent Promise
      ↓
Child Must Honor It

If Child Changes Behavior
      ↓
LSP Violation