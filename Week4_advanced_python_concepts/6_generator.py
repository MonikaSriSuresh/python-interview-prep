"""
06_Generators.py
"""


# ==================================================
# Example 1 - Basic Generator
# ==================================================

def numbers():

    yield 1
    yield 2
    yield 3


g = numbers()

print("Example 1")

print(next(g))
print(next(g))
print(next(g))


# ==================================================
# Example 2 - Pause And Resume
# ==================================================

def test():

    print("A")

    yield 1

    print("B")

    yield 2


g = test()

print("\nExample 2")

print(next(g))

print(next(g))


# ==================================================
# Example 3 - Generator In Loop
# ==================================================

def count():

    yield 1
    yield 2
    yield 3


print("\nExample 3")

for x in count():
    print(x)


# ==================================================
# Example 4 - Generator Expression
# ==================================================

g = (i for i in range(5))

print("\nExample 4")

print(next(g))
print(next(g))
print(next(g))


# ==================================================
# Example 5 - Memory Efficient
# ==================================================

def large_numbers():

    for i in range(1000000):

        yield i


g = large_numbers()

print("\nExample 5")

print(next(g))
print(next(g))
print(next(g))


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
# Example 7 - Generator Is Iterator
# ==================================================

g = numbers()

print("\nExample 7")

print(next(g))


# ==================================================
# Interview Question
# ==================================================

def interview():

    yield 10

    yield 20

    yield 30


g = interview()

print("\nInterview Question")

print(next(g))
print(next(g))
print(next(g))


"""
REVISION NOTES

Generator

def numbers():

    yield 1

Generator Object

g = numbers()

next(g)

returns next value

Generator

yield value
pause

next()
resume

Every Generator Is Iterator

Not Every Iterator Is Generator

Generator Expression

(i for i in range(5))

List Comprehension

[i for i in range(5)]

Generator saves memory.
"""