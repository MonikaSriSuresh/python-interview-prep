# README.md

# Advanced Python - Revision Notes

## Topics Covered

### 1. Functions as Objects

* Functions are first-class objects.
* Can be assigned to variables.
* Can be passed as arguments.
* Can be returned from functions.

### 2. Closures

* Inner functions remember variables from outer scope.
* Variables survive even after outer function execution ends.

### 3. Decorators

* Functions that wrap other functions.
* Add behavior without modifying original code.
* Implemented using closures.

### 4. Decorators with Arguments

* Require three nested functions.
* Outer function accepts decorator arguments.
* Middle function accepts decorated function.
* Inner wrapper executes logic.

### 5. Iterable vs Iterator

* Iterable = collection.
* Iterator = remembers current position.
* Uses iter() and next().

### 6. Generators

* Special iterators created using yield.
* Generate values lazily.
* Memory efficient.

### 7. yield vs return

* return terminates function.
* yield pauses function and preserves state.

## Interview Formula

Functions as Objects
↓
Passing Functions
↓
Returning Functions
↓
Closures
↓
Decorators
↓
Decorators With Arguments

Iterable
↓ iter()
Iterator
↓ next()
Values
↓
StopIteration

Generator
↓
Special Iterator
↓
yield
↓
Pause + Resume
