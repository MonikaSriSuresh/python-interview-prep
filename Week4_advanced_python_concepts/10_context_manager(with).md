# Topic 10: Context Managers (with)

## Why Context Managers?

Problem:

```python
file = open("data.txt")

data = file.read()

file.close()
```

What if an exception occurs before `file.close()`?

```python
file = open("data.txt")

x = 10 / 0

file.close()
```

Execution:

File Opened
↓
ZeroDivisionError
↓
Program Crashes
↓
file.close() Never Executes

Result:

Resource Leak

Examples of Resources:

* Files
* Database Connections
* Network Connections
* Sockets
* Locks

---

## Solution: Context Manager

```python
with open("data.txt") as file:
    data = file.read()
```

Execution:

Open File
↓
Execute Block
↓
Automatically Close File

Even if an exception occurs:

Open File
↓
Exception Occurs
↓
File Automatically Closed
↓
Exception Propagates

---

## Why Use with?

Interview Answer:

Context managers automatically manage resources.

They ensure cleanup happens even if an exception occurs.

This prevents resource leaks.

---

## Context Manager vs try-finally

### Using try-finally

```python
file = open("data.txt")

try:
    data = file.read()

finally:
    file.close()
```

### Using with

```python
with open("data.txt") as file:
    data = file.read()
```

Both guarantee cleanup.

Difference:

* try-finally = Manual Cleanup
* with = Automatic Cleanup

---

## File Status Example

```python
with open("data.txt") as file:

    print(file.closed)

print(file.closed)
```

Output:

False
True

Explanation:

Inside with block:

File is open

Outside with block:

File is automatically closed

---

## Variable vs Resource

Many beginners think:

```python
with open("data.txt") as file:
    pass
```

removes file completely.

Wrong.

After the with block:

```python
print(file.closed)
```

works.

Variable exists.

But:

Resource is closed.

Remember:

Variable Exists
≠
Resource Open

---

## Reading After File Is Closed

```python
with open("data.txt") as file:
    pass

print(file.read())
```

Execution:

Open File
↓
Exit with block
↓
File Closed
↓
file.read()
↓
ValueError

Exception:

ValueError:
I/O operation on closed file

---

## FileNotFoundError vs Closed File Error

Case 1:

```python
open("missing.txt")
```

Exception:

FileNotFoundError

Reason:

File never opened.

Case 2:

```python
with open("data.txt") as file:
    pass

file.read()
```

Exception:

ValueError

Reason:

File opened successfully but is now closed.

---

## with and finally

```python
with open("data.txt") as file:

    try:
        x = 10 / 0

    finally:
        print("Finally")
```

Execution:

Open File
↓
Enter try
↓
ZeroDivisionError
↓
finally Executes
↓
Exit try-finally
↓
Exit with Block
↓
File Closed
↓
Exception Propagates

Output:

Finally
ZeroDivisionError

Rule:

finally executes first

then context manager cleanup occurs

---

## Interview Questions

### Q1 Why use with?

To automatically manage resources and ensure cleanup.

---

### Q2 Does with close files even when exceptions occur?

Yes.

---

### Q3 Is file variable destroyed after with?

No.

Variable exists.

Resource is closed.

---

### Q4 What does file.closed return?

True if file is closed.

False if file is open.

---

### Q5 Difference between with and try-finally?

try-finally:
Manual Cleanup

with:
Automatic Cleanup

---

## Quick Revision

with
↓
Context Manager

Context Manager
↓
Automatic Resource Management

Automatic Resource Management
↓
Open / Close
Connect / Disconnect
Acquire / Release

Benefits:

✓ Cleaner Code

✓ Automatic Cleanup

✓ Exception Safe

✓ Prevents Resource Leaks
