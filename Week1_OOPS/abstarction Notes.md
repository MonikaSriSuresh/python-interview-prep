# Abstraction Notes

## What is Abstraction?

**Definition:**

Abstraction is the process of hiding implementation details and exposing only the essential functionality to the user.

In simple words:

```text
Show WHAT to do
Hide HOW it is done
```

---

## Why Do We Need Abstraction?

Without abstraction, users and developers would need to understand every internal implementation detail.

Abstraction helps by:

* Hiding complexity
* Providing a simple interface
* Improving maintainability
* Reducing dependency on internal implementation

---

## Real-World Example 1: ATM

When using an ATM:

1. Insert Card
2. Enter PIN
3. Withdraw Money

As a user, you do not know:

* How the PIN is validated
* How the database is queried
* How the balance is updated
* How the transaction is logged

You only see:

```text
Withdraw Money
```

The internal complexity is hidden.

This is Abstraction.

---

## Real-World Example 2: Car

User Action:

```python
car.start()
```

The user does not know:

* How fuel enters the engine
* How ignition works
* How combustion happens
* How pistons move

The user only knows:

```python
car.start()
```

The implementation details are hidden.

This is Abstraction.

---

## Abstraction in Software

Suppose you are using a payment gateway.

You simply do:

```python
payment.pay(1000)
```

Internally, the system may:

```text
Validate Card
Authenticate User
Check Balance
Connect to Bank
Deduct Amount
Generate Transaction ID
Send Notification
```

The user does not need to know these steps.

The user only sees:

```python
payment.pay()
```

This is Abstraction.

---

## Encapsulation vs Abstraction

### Encapsulation

Focus:

```text
Protect Data
```

Question:

```text
Who can access the data?
```

Example:

```python
self.__balance
```

Purpose:

* Restrict access
* Protect data

---

### Abstraction

Focus:

```text
Hide Complexity
```

Question:

```text
How can implementation details be hidden?
```

Example:

```python
car.start()
```

Purpose:

* Hide internal implementation
* Expose only essential functionality

---

## How Python Implements Abstraction

Python provides abstraction through:

```python
from abc import ABC, abstractmethod
```

Where:

```text
ABC = Abstract Base Class
```

---

## Abstract Class

An abstract class is a class that cannot be instantiated directly.

Example:

```python
from abc import ABC

class Payment(ABC):
    pass
```

Invalid:

```python
payment = Payment()
```

Output:

```text
TypeError
```

Reason:

The abstract class is intended to act as a blueprint for child classes.

---

## Abstract Method

An abstract method is a method declared without implementation.

Example:

```python
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass
```

Notice:

```python
def pay(self):
    pass
```

There is no implementation.

It only defines a contract that child classes must follow.

---

## Why Use Abstract Methods?

Suppose an application supports:

```text
Credit Card
UPI
Net Banking
PayPal
```

Every payment type must implement:

```python
pay()
```

Abstract methods enforce this rule.

---

## Complete Example

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class UPIPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using UPI")
```

Usage:

```python
credit = CreditCardPayment()
credit.pay(1000)

upi = UPIPayment()
upi.pay(500)
```

Output:

```text
Paid 1000 using Credit Card
Paid 500 using UPI
```

---

## What Happens If a Child Class Does Not Implement an Abstract Method?

Example:

```python
class CreditCardPayment(Payment):
    pass
```

Now:

```python
credit = CreditCardPayment()
```

Output:

```text
TypeError:
Can't instantiate abstract class CreditCardPayment
with abstract method pay
```

Reason:

Python forces every child class to implement all abstract methods.

This is known as enforcing a contract.

---

## Real-World BACI Example

Suppose BACI has multiple document processors.

```text
PDF Processor
Excel Processor
Word Processor
```

Every processor must implement:

```python
process_document()
```

Abstract Class:

```python
from abc import ABC, abstractmethod

class DocumentProcessor(ABC):

    @abstractmethod
    def process_document(self):
        pass
```

PDF Processor:

```python
class PDFProcessor(DocumentProcessor):

    def process_document(self):
        print("Processing PDF")
```

Excel Processor:

```python
class ExcelProcessor(DocumentProcessor):

    def process_document(self):
        print("Processing Excel")
```

Now every processor is guaranteed to have:

```python
process_document()
```

This pattern is heavily used in enterprise applications.

---

## Advantages of Abstraction

### 1. Hides Complexity

User sees:

```python
payment.pay()
```

Not the internal implementation.

---

### 2. Provides a Standard Interface

All payment classes must implement:

```python
pay()
```

---

### 3. Improves Maintainability

Implementation can change without affecting users.

---

### 4. Reduces Coupling

Users depend on interfaces rather than implementations.

---

## Interview Questions

### What is Abstraction?

Abstraction is an OOP principle that hides implementation details and exposes only essential functionality to the user.

---

### What is an Abstract Class?

An abstract class is a class that contains one or more abstract methods and cannot be instantiated directly.

---

### What is an Abstract Method?

An abstract method is a method declared without implementation that must be implemented by child classes.

---

## Difference Between Encapsulation and Abstraction

| Encapsulation             | Abstraction                 |
| ------------------------- | --------------------------- |
| Protects Data             | Hides Complexity            |
| Uses Private Variables    | Uses Abstract Classes       |
| Focuses on Access Control | Focuses on Interface Design |
| Example: `__balance`      | Example: `pay()`            |

---

## Senior-Level Interview Answer

Abstraction is the process of exposing only the necessary functionality while hiding internal implementation details. For example, in a payment system, users simply call `pay(amount)` without knowing the internal steps such as authentication, validation, transaction processing, and notification handling. In Python, abstraction is commonly implemented using abstract classes and abstract methods from the `abc` module to define contracts that child classes must implement.
