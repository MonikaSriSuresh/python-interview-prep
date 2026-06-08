# Interface Segregation Principle (ISP)

## Definition

Do not force classes to implement methods they do not need.

## Bad Example

```python
class Worker:

    def work(self):
        pass

    def eat(self):
        pass
```

Robot forced to implement eat().

ISP Violation.

## Good Example

```python
class Workable:
    pass


class Eatable:
    pass
```

Small interfaces.

Specific responsibilities.

## Interview Answer

Large interfaces should be split into smaller and more specific interfaces.

## Revision

Don't Force Classes

To Implement Unused Methods