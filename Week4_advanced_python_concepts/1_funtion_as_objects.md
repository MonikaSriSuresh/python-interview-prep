# 01_Functions_As_Objects.md

# Functions as Objects

## Definition

Python treats functions as first-class objects.

This means functions can:

* Be assigned to variables
* Be passed as arguments
* Be returned from other functions
* Be stored in data structures

## Why Needed?

Without first-class functions:

* Decorators would not exist
* Callbacks would not exist
* Higher-order functions would not exist

Many Python features depend on functions being objects.

## Example 1 - Assigning Function to Variable

```python
def greet():
    print("Hello")

x = greet

x()
```

### Output

```text
Hello
```

## Memory Diagram

```text
greet
  |
  v
Function Object
  ^
  |
  x
```

Both variables point to the same function object.

## Example 2 - Printing Function Object

```python
def greet():
    print("Hello")

print(greet)
```

### Output

```text
<function greet at 0x...>
```

The memory address changes every run.

## Example 3 - Passing Function as Argument

```python
def greet():
    print("Hello")

def execute(func):
    func()

execute(greet)
```

### Output

```text
Hello
```

## Why Does This Work?

Because:

```python
execute(greet)
```

passes the function object.

Inside:

```python
func = greet
```

Then:

```python
func()
```

becomes:

```python
greet()
```

## Example 4 - Returning Functions

```python
def outer():

    def inner():
        print("Hello")

    return inner

x = outer()

x()
```

### Output

```text
Hello
```

## Interview Questions

### Q1

What are first-class functions?

Answer:

Functions that can be assigned, passed and returned like any other object.

### Q2

Difference between:

```python
greet
```

and

```python
greet()
```

Answer:

greet -> function object

greet() -> executes function

## Key Takeaways

✓ Functions are objects

✓ Can be assigned

✓ Can be passed

✓ Can be returned

✓ Foundation for decorators
