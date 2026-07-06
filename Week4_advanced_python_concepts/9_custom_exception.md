# Topic 9: Custom Exceptions

## Why Custom Exceptions?

Python provides built-in exceptions:

* ValueError
* TypeError
* KeyError
* IndexError
* ZeroDivisionError
* FileNotFoundError

Sometimes business rules require custom exceptions.

Example:

Bank Account

Balance = 1000

Withdraw = 5000

Technically:

5000 is a valid integer.

No ValueError occurs.

But business-wise:

Insufficient Balance

So we create our own exception.

---

## Creating a Custom Exception

```python
class InsufficientBalanceError(Exception):
    pass
```

Inheritance:

Exception
↓
InsufficientBalanceError

Reason:

Exception is the base class for most Python exceptions.

By inheriting from Exception, Python treats our class as a valid exception.

---

## Raising an Exception

```python
raise ValueError("Invalid Input")
```

Meaning:

Create Exception Object
↓
Throw Exception

---

## Raising a Custom Exception

```python
class InsufficientBalanceError(Exception):
    pass

raise InsufficientBalanceError("Balance Low")
```

Execution:

Create InsufficientBalanceError Object
↓
Store Message
↓
Throw Exception

---

## What Does raise Do?

Interview Answer:

raise creates and throws an exception.

Example:

```python
raise ValueError("Age cannot be negative")
```

Creates:

ValueError Object
↓
message = "Age cannot be negative"

Then throws it.

---

## Catching Custom Exceptions

```python
class InsufficientBalanceError(Exception):
    pass

try:

    raise InsufficientBalanceError("Balance Low")

except InsufficientBalanceError:

    print("Cannot Withdraw")
```

Output:

Cannot Withdraw

---

## What is 'as e'?

```python
try:

    raise ValueError("Invalid Age")

except ValueError as e:

    print(e)
```

Meaning:

e
↓
Reference to Exception Object

---

## Memory Diagram

```python
raise ValueError("Invalid Age")
```

Creates:

ValueError Object
↓
message = "Invalid Age"

Then:

```python
except ValueError as e:
```

e
↓
ValueError Object
↓
message = "Invalid Age"

---

## print(e)

```python
try:

    raise ValueError("Invalid Age")

except ValueError as e:

    print(e)
```

Output:

Invalid Age

Reason:

Python prints the stored exception message.

---

## type(e)

```python
try:

    raise ValueError("Invalid Age")

except ValueError as e:

    print(type(e))
```

Output:

<class 'ValueError'>

Reason:

type() returns the class of the object.

---

## Exception Hierarchy

BaseException
↓
Exception
↓
├── ValueError
├── TypeError
├── KeyError
├── IndexError
├── ZeroDivisionError
└── Custom Exceptions

Example:

```python
class AgeError(Exception):
    pass
```

Hierarchy:

Exception
↓
AgeError

---

## Why except Exception Catches Custom Exceptions

```python
class AgeError(Exception):
    pass

try:

    raise AgeError("Age must be above 18")

except Exception as e:

    print(e)
```

Output:

Age must be above 18

Reason:

AgeError inherits from Exception.

AgeError IS-A Exception.

---

## Exception Object vs Message

Wrong:

e = Message

Correct:

e = Exception Object

Example:

e
↓
AgeError Object
↓
message = "Age must be above 18"

---

## Program Crash Example

```python
class AgeError(Exception):
    pass

raise AgeError("Invalid Age")
```

Execution:

Create Exception Object
↓
Throw Exception
↓
No Matching except
↓
Program Crashes

---

## Interview Questions

### Why create custom exceptions?

To represent business-specific errors.

---

### Why inherit from Exception?

Because Exception is the base class for Python exceptions.

---

### What does raise do?

Creates and throws an exception.

---

### What is except Exception as e?

Catches exception object and stores it in e.

---

### What is print(e)?

Prints exception message.

---

### What is type(e)?

Returns exception class.

---

## Quick Revision

Custom Exception
↓
class MyError(Exception)

raise
↓
Create + Throw Exception

except MyError
↓
Catch Exception

except MyError as e
↓
Catch Exception Object

print(e)
↓
Exception Message

type(e)
↓
Exception Class
