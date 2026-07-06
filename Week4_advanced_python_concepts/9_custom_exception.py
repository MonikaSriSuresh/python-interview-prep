# =====================================================
# Topic 9 - Custom Exceptions
# Save as: custom_exceptions.py
# =====================================================

print("===== Example 1 : Creating a Custom Exception =====")

class AgeError(Exception):
    pass

try:
    raise AgeError("Age must be above 18")

except AgeError:
    print("Custom Exception Caught")


# =====================================================

print("\n===== Example 2 : ValueError Object =====")

try:
    raise ValueError("Invalid Age")

except ValueError as e:
    print(type(e))
    print(e)


# =====================================================

print("\n===== Example 3 : Custom Exception Object =====")

class InsufficientBalanceError(Exception):
    pass

try:
    raise InsufficientBalanceError("Balance Low")

except InsufficientBalanceError as e:
    print(type(e))
    print(e)


# =====================================================

print("\n===== Example 4 : Parent Exception Catching Child =====")

class AgeError(Exception):
    pass

try:
    raise AgeError("Age must be above 18")

except Exception as e:
    print(type(e))
    print(e)


# =====================================================

print("\n===== Example 5 : ValueError Caught By Parent Exception =====")

try:
    raise ValueError("Invalid Input")

except Exception as e:
    print("Caught By Parent Exception")
    print(type(e))
    print(e)


# =====================================================

print("\n===== Example 6 : Business Rule Exception =====")

class SalaryError(Exception):
    pass

salary = 5000

try:
    if salary < 10000:
        raise SalaryError("Salary Too Low")

except SalaryError as e:
    print(type(e))
    print(e)


# =====================================================

print("\n===== Example 7 : Login Exception =====")

class LoginError(Exception):
    pass

try:
    raise LoginError("Invalid Credentials")

except LoginError as e:
    print("Exception Class:", type(e))
    print("Exception Message:", e)


# =====================================================

print("\n===== Example 8 : Program Crash Example =====")

class DemoError(Exception):
    pass

try:
    raise DemoError("Demo Error Occurred")

except DemoError as e:
    print("Caught:", e)


# =====================================================

print("\n===== Example 9 : Exception Object =====")

try:
    raise ValueError("Invalid Number")

except ValueError as e:
    print("e =", e)
    print("type(e) =", type(e))


# =====================================================

print("\n===== Example 10 : Interview Revision =====")

print("raise = Create + Throw Exception")
print("except = Catch Exception")
print("e = Exception Object")
print("print(e) = Exception Message")
print("type(e) = Exception Class")
print("Custom Exceptions Inherit From Exception")
print("Exception Can Catch Child Exceptions")
print("If No Matching except Exists -> Program Crashes")


# =====================================================
# End of File
# =====================================================