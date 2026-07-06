# =====================================================
# Topic 8 - Exception Handling
# =====================================================

print("===== Example 1 =====")

try:
    print("Start")
    x = 10 / 0
    print("End")

except ZeroDivisionError:
    print("Cannot Divide By Zero")

print("Program Continues")


print("\n===== Example 2 =====")

try:
    x = 10 / 2
    print("A")

except ZeroDivisionError:
    print("B")

print("C")


print("\n===== Example 3 =====")

try:
    int("abc")

except ValueError:
    print("Invalid Number")


print("\n===== Example 4 =====")

try:
    int("abc")

except ValueError:
    print("ValueError Handled")

except ZeroDivisionError:
    print("ZeroDivisionError Handled")

print("End")


print("\n===== Example 5 =====")

try:
    x = 10 / 0

except Exception:
    print("Generic Exception Handler")


print("\n===== Example 6 =====")

try:
    x = 10 / 0

except Exception as e:
    print(type(e))
    print(e)


print("\n===== Example 7 =====")

try:
    x = 10 / 2

except ZeroDivisionError:
    print("Cannot Divide")

else:
    print("Success")


print("\n===== Example 8 =====")

try:
    x = 10 / 0

except ZeroDivisionError:
    print("Cannot Divide")

else:
    print("Success")


print("\n===== Example 9 =====")

try:
    x = 10 / 0

except ZeroDivisionError:
    print("Cannot Divide")

finally:
    print("Cleanup")


print("\n===== Example 10 =====")

try:
    x = 10 / 2

finally:
    print("Cleanup")


print("\n===== Example 11 =====")

try:
    x = 10 / 0

except ZeroDivisionError:
    print("Error")

finally:
    print("Finally")


print("\n===== Example 12 =====")

try:
    x = 10 / 2

except ZeroDivisionError:
    print("Error")

else:
    print("Success")

finally:
    print("Cleanup")


print("\n===== Example 13 =====")

try:
    int("abc")

except ValueError as e:
    print(type(e))
    print(e)


print("\n===== Example 14 =====")

try:
    int("abc")

except ValueError:
    print("ValueError")

except TypeError:
    print("TypeError")

except Exception:
    print("Generic Exception")


print("\n===== Example 15 =====")

try:
    int("abc")

except Exception:
    print("Caught By Parent Exception")


print("\n===== Interview Revision =====")

print("try = Risky Code")
print("except = Handle Exception")
print("else = Runs Only When No Exception Occurs")
print("finally = Always Executes")
print("Exception = Parent Class")
print("e = Exception Object")
print("print(e) = Exception Message")
print("type(e) = Exception Class")

# =====================================================
# End Of File
# =====================================================