"""
Access Modifiers in Python
Public, Protected, Private
"""

# ==================================================
# 1. PUBLIC MEMBERS
# ==================================================

print("===== PUBLIC MEMBER =====")


class Employee:

    def __init__(self):
        self.name = "Monika"


emp = Employee()

print(emp.name)

print()

# ==================================================
# 2. PROTECTED MEMBERS
# ==================================================

print("===== PROTECTED MEMBER =====")


class Employee:

    def __init__(self):
        self._salary = 100000


emp = Employee()

print(emp._salary)

print()

# ==================================================
# 3. PROTECTED MEMBER IN INHERITANCE
# ==================================================

print("===== PROTECTED + INHERITANCE =====")


class Employee:

    def __init__(self):
        self._salary = 100000


class Developer(Employee):

    def show_salary(self):
        print(self._salary)


dev = Developer()

dev.show_salary()

print()

# ==================================================
# 4. PRIVATE MEMBERS
# ==================================================

print("===== PRIVATE MEMBER =====")


class Employee:

    def __init__(self):
        self.__salary = 100000


emp = Employee()

# print(emp.__salary)
# AttributeError

print()

# ==================================================
# 5. NAME MANGLING
# ==================================================

print("===== NAME MANGLING =====")


class Employee:

    def __init__(self):
        self.__salary = 100000


emp = Employee()

print(emp.__dict__)

print()

# ==================================================
# 6. ACCESSING PRIVATE VARIABLE
# ==================================================

print("===== ACCESS PRIVATE VARIABLE =====")


class Employee:

    def __init__(self):
        self.__salary = 100000


emp = Employee()

print(emp._Employee__salary)

print()

# ==================================================
# 7. PUBLIC vs PROTECTED vs PRIVATE
# ==================================================

print("===== COMPARISON =====")


class Employee:

    def __init__(self):

        self.name = "Monika"           # Public

        self._department = "IT"        # Protected

        self.__salary = 100000         # Private


emp = Employee()

print("Public:", emp.name)

print("Protected:", emp._department)

print("Private:", emp._Employee__salary)

print()

# ==================================================
# 8. INTERVIEW EXAMPLE
# ==================================================

print("===== INTERVIEW EXAMPLE =====")


class BankAccount:

    def __init__(self):

        self.account_holder = "Monika"

        self._account_type = "Savings"

        self.__balance = 50000

    def show_balance(self):
        print(self.__balance)


account = BankAccount()

print(account.account_holder)

print(account._account_type)

account.show_balance()