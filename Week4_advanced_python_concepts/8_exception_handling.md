# Topic 8: Exception Handling

## What is an Exception?

An exception is a runtime error that interrupts normal program execution.

Example:

```python
x = 10 / 0
```

Output:

```text
ZeroDivisionError
```

Execution:

Program Starts
↓
10 / 0
↓
Exception Occurs
↓
Program Stops

---

## try and except

```python
try:
    x = 10 / 0

except ZeroDivisionError:
    print("Cannot Divide By Zero")
```

Execution:

try Block
↓
Exception Occurs
↓
Matching except Found
↓
Exception Handled
↓
Program Continues

Output:

Cannot Divide By Zero

---

## Unhandled Exception

```python
try:
    int("abc")

except ZeroDivisionError:
    print("Cannot Divide")
```

Execution:

ValueError Occurs
↓
No Matching except
↓
Program Crashes

Output:

ValueError

---

## Multiple except Blocks

```python
try:
    int("abc")

except ValueError:
    print("Invalid Number")

except ZeroDivisionError:
    print("Cannot Divide")
```

Output:

Invalid Number

Rule:

Python executes the first matching except block.

---

## Generic Exception

```python
try:
    x = 10 / 0

except Exception:
    print("Generic Handler")
```

Output:

Generic Handler

Reason:

Exception is the parent class of most Python exceptions.

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
└── FileNotFoundError

---

## else Block

```python
try:
    x = 10 / 2

except ZeroDivisionError:
    print("Cannot Divide")

else:
    print("Success")
```

Output:

Success

Rule:

else executes only when no exception occurs.

---

## else Example With Exception

```python
try:
    x = 10 / 0

except ZeroDivisionError:
    print("Cannot Divide")

else:
    print("Success")
```

Output:

Cannot Divide

Rule:

If exception occurs, else does not execute.

---

## finally Block

```python
try:
    x = 10 / 0

except ZeroDivisionError:
    print("Cannot Divide")

finally:
    print("Cleanup")
```

Output:

Cannot Divide
Cleanup

Rule:

finally always executes.

---

## finally Without Exception

```python
try:
    x = 10 / 2

finally:
    print("Cleanup")
```

Output:

Cleanup

Rule:

finally executes whether exception occurs or not.

---

## try-except-else-finally Flow

```python
try:
    x = 10 / 2

except ZeroDivisionError:
    print("Error")

else:
    print("Success")

finally:
    print("Cleanup")
```

Execution:

try
↓
No Exception
↓
else
↓
finally

Output:

Success
Cleanup

---

## except as e

```python
try:
    int("abc")

except ValueError as e:
    print(type(e))
    print(e)
```

Output:

<class 'ValueError'>
invalid literal for int()

Meaning:

e
↓
Exception Object

---

## Interview Questions

### What is an exception?

Runtime error that interrupts normal execution.

### Why use try-except?

To handle exceptions and prevent program crashes.

### When does else execute?

Only when no exception occurs.

### When does finally execute?

Always.

### Why use Exception?

To catch any unexpected exception.

### What is e in except Exception as e?

Reference to exception object.

---

## Quick Revision

try
↓
Risky Code

except
↓
Handle Exception

else
↓
Runs When No Exception Occurs

finally
↓
Always Executes

Exception
↓
Parent Class Of Most Exceptions
