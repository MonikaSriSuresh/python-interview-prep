# Open Closed Principle (OCP)

## Definition

Open for Extension

Closed for Modification

## Meaning

Add new functionality without changing existing code.

## Bad Example

```python
if payment_type == "UPI":
    pass

elif payment_type == "CARD":
    pass
```

Need to modify code for every new payment method.

OCP Violation.

## Good Example

```python
class Payment:
    pass

class UPIPayment(Payment):
    pass

class CardPayment(Payment):
    pass
```

Add new classes.

No modification required.

## Interview Answer

Software entities should be open for extension and closed for modification.

## Revision

Extend Code

Do Not Modify Existing Code