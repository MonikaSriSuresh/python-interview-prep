# Factory Pattern

## Definition

Factory Pattern centralizes object creation logic and hides the object creation details from the client.

---

## Problem

Object creation is scattered throughout the application.

```python
if payment_type == "UPI":
    payment = UPIPayment()

elif payment_type == "CARD":
    payment = CardPayment()
```

This violates Open Closed Principle.

---

## Solution

Move object creation into a dedicated Factory class.

---

## Structure

### Product Interface

```python
class Payment:
    pass
```

### Concrete Products

```python
class UPIPayment:
    pass

class CardPayment:
    pass
```

### Factory

```python
class PaymentFactory:
    pass
```

---

## Benefits

* Centralized Object Creation
* Reduced Coupling
* Easier Maintenance
* Better Scalability
* Supports OCP

---

## Drawbacks

* Additional Class
* Factory may become large if poorly designed

---

## Real-World Examples

* Payment Systems
* Notification Systems
* Vehicle Creation
* Report Generation

---

## Interview Answer

Factory Pattern hides object creation logic and centralizes it in one place, reducing coupling and improving maintainability.
