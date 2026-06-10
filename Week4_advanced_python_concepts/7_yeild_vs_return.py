"""
07_Yield_vs_Return.py
"""


# ==================================================
# Example 1 - return
# ==================================================

def return_example():

    print("Before Return")

    return 10

    print("After Return")


print("Example 1")

print(return_example())


# ==================================================
# Example 2 - yield
# ==================================================

def yield_example():

    print("Before Yield")

    yield 10

    print("After Yield")


g = yield_example()

print("\nExample 2")

print(next(g))


# ==================================================
# Example 3 - Pause And Resume
# ==================================================

def pause_resume():

    print("A")

    yield 1

    print("B")

    yield 2

    print("C")

    yield 3


g = pause_resume()

print("\nExample 3")

print(next(g))
print(next(g))
print(next(g))


# ==================================================
# Example 4 - State Preservation
# ==================================================

def counter():

    x = 1

    yield x

    x += 1

    yield x

    x += 1

    yield x


g = counter()

print("\nExample 4")

print(next(g))
print(next(g))
print(next(g))


# ==================================================
# Example 5 - Multiple Yields
# ==================================================

def numbers():

    yield 10

    yield 20

    yield 30


print("\nExample 5")

for num in numbers():

    print(num)


# ==================================================
# Example 6 - StopIteration
# ==================================================

def sample():

    yield 1


g = sample()

print("\nExample 6")

print(next(g))

try:

    print(next(g))

except StopIteration:

    print("StopIteration Raised")


# ==================================================
# Example 7 - Generator Object
# ==================================================

def test():

    yield 100


g = test()

print("\nExample 7")

print(g)

print(next(g))


# ==================================================
# Interview Question 1
# ==================================================

def interview():

    print("Start")

    yield 1

    print("Middle")

    yield 2


g = interview()

print("\nInterview Question 1")

print(next(g))

print(next(g))


# ==================================================
# Interview Question 2
# ==================================================

def square_numbers():

    for i in range(5):

        yield i * i


print("\nInterview Question 2")

for num in square_numbers():

    print(num)


"""
REVISION NOTES

return

return value
↓
function ends
↓
state destroyed


yield

yield value
↓
pause
↓
next()
↓
resume
↓
state preserved


return
    -> one final result

yield
    -> multiple values over time


Generator Function

def test():

    yield 1

returns

Generator Object


Most Important Interview Answer

return terminates the function and destroys its state.

yield pauses the function, preserves its state,
and allows execution to resume later.
"""