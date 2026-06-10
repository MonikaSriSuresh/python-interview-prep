# Strategy Pattern

## Definition

Strategy Pattern defines a family of algorithms, encapsulates each algorithm into separate classes, and makes them interchangeable at runtime.

---

## Problem

Large if-elif chains.

```python
if payment_type == "UPI":
    process_upi()

elif payment_type == "CARD":
    process_card()

elif payment_type == "WALLET":
    process_wallet()
```

As the application grows, the conditional chain becomes difficult to maintain.

---

## Solution

Move each behavior into a separate class.

---

## Structure

### Strategy Interface

```python
class PaymentStrategy:
    pass
```

### Concrete Strategies

```python
class UPIPayment:
    pass

class CardPayment:
    pass
```

### Context

```python
class PaymentProcessor:
    pass
```

---

## Benefits

* Eliminates Large if-elif Chains
* Supports OCP
* Easier Testing
* Easier Maintenance
* Runtime Flexibility

---

## Drawbacks

* More Classes
* Slightly More Complex Design

---

## Real-World Examples

* Payment Processing
* Discount Calculation
* Route Planning
* File Compression

---

## Interview Answer

Strategy Pattern encapsulates multiple algorithms into separate classes and allows them to be selected at runtime without modifying existing code.
