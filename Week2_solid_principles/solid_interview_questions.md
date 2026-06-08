# SOLID Interview Questions

## SRP

Q: What is SRP?

A: A class should have only one responsibility and one reason to change.

---

## OCP

Q: What is OCP?

A: Open for Extension, Closed for Modification.

---

## LSP

Q: What is LSP?

A: Child classes should replace parent classes without breaking behavior.

---

## ISP

Q: What is ISP?

A: Classes should not be forced to implement methods they do not need.

---

## DIP

Q: What is DIP?

A: Depend on abstractions rather than concrete implementations.

---

## Which SOLID Principle is violated?

Bird -> Penguin

Answer:
LSP

---

## Which SOLID Principle is violated?

Robot forced to implement eat()

Answer:
ISP

---

## Which SOLID Principle is violated?

Need to modify if-else chain for every new payment method.

Answer:
OCP

---

## Which SOLID Principle is violated?

UserService directly creates MySQLDatabase()

Answer:
DIP

---

## Which SOLID Principle is violated?

Employee class calculates salary and saves to database.

Answer:
SRP