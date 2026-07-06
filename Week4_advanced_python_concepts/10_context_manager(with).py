# =====================================================
# Topic 10 - Context Managers (with)
# Save as: context_manager.py
# =====================================================

print("===== Example 1 : Basic Context Manager =====")

with open("sample.txt", "w") as file:
    file.write("Hello Context Manager")

print("File Automatically Closed")


# =====================================================

print("\n===== Example 2 : File Status =====")

with open("sample.txt", "r") as file:

    print("Inside With Block")
    print("file.closed =", file.closed)

print("Outside With Block")
print("file.closed =", file.closed)


# =====================================================

print("\n===== Example 3 : Exception Inside With =====")

try:

    with open("sample.txt", "r") as file:

        print("File Opened")

        x = 10 / 0

except ZeroDivisionError:

    print("Division By Zero Caught")

print("Program Continues")


# =====================================================

print("\n===== Example 4 : Reading Closed File =====")

try:

    with open("sample.txt", "r") as file:

        print("Reading File")

    file.read()

except Exception as e:

    print(type(e))
    print(e)


# =====================================================

print("\n===== Example 5 : With And Finally =====")

try:

    with open("sample.txt", "r") as file:

        try:

            x = 10 / 0

        finally:

            print("Finally Executed")

except Exception as e:

    print(type(e))
    print(e)


# =====================================================

print("\n===== Example 6 : try-finally Cleanup =====")

file = open("sample.txt", "r")

try:

    data = file.read()

finally:

    file.close()

print("File Closed Using try-finally")


# =====================================================

print("\n===== Example 7 : with Cleanup =====")

with open("sample.txt", "r") as file:

    data = file.read()

print("File Closed Using Context Manager")


# =====================================================

print("\n===== Example 8 : Variable Exists After With =====")

with open("sample.txt", "r") as file:

    print("Inside Block")

print("Variable Exists:", file)
print("File Closed:", file.closed)


# =====================================================

print("\n===== Example 9 : File Status Demo =====")

with open("sample.txt", "r") as file:

    print("Inside Block:", file.closed)

print("Outside Block:", file.closed)


# =====================================================

print("\n===== Example 10 : Resource Leak Problem =====")

try:

    file = open("sample.txt", "r")

    x = 10 / 0

    file.close()

except Exception as e:

    print(type(e))
    print("file.close() never executed")


# =====================================================

print("\n===== Example 11 : Context Manager Prevents Leak =====")

try:

    with open("sample.txt", "r") as file:

        x = 10 / 0

except Exception as e:

    print(type(e))
    print("File Automatically Closed")


# =====================================================

print("\n===== Example 12 : Interview Revision =====")

print("with = Context Manager")
print("Context Manager = Automatic Resource Management")
print("Prevents Resource Leaks")
print("Automatically Closes Files")
print("Works Even During Exceptions")
print("Similar To try-finally")
print("Variable Can Exist After With")
print("Resource Is Closed After With")


# =====================================================
# End Of File
# =====================================================
