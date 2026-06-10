"""
05_Iterable_Iterator.py
"""


# ==================================================
# Example 1 - Iterable
# ==================================================

nums = [1, 2, 3]

print("Example 1")

for x in nums:
    print(x)


# ==================================================
# Example 2 - Iterator Creation
# ==================================================

nums = [1, 2, 3]

it = iter(nums)

print("\nExample 2")

print(it)


# ==================================================
# Example 3 - next()
# ==================================================

nums = [1, 2, 3]

it = iter(nums)

print("\nExample 3")

print(next(it))
print(next(it))
print(next(it))


# ==================================================
# Example 4 - Iterator Remembers Position
# ==================================================

nums = [1, 2, 3]

it = iter(nums)

print("\nExample 4")

print(next(it))
print(next(it))


# ==================================================
# Example 5 - Multiple Iterators
# ==================================================

nums = [1, 2, 3]

it1 = iter(nums)
it2 = iter(nums)

print("\nExample 5")

print(next(it1))
print(next(it2))
print(next(it1))


# ==================================================
# Example 6 - StopIteration
# ==================================================

nums = [1]

it = iter(nums)

print("\nExample 6")

print(next(it))

try:
    print(next(it))
except StopIteration:
    print("StopIteration Raised")


# ==================================================
# Example 7 - Internal For Loop
# ==================================================

nums = [10, 20, 30]

it = iter(nums)

print("\nExample 7")

while True:

    try:

        value = next(it)

        print(value)

    except StopIteration:

        break


# ==================================================
# Interview Question
# ==================================================

nums = [100, 200]

it = iter(nums)

print("\nInterview Question")

print(next(it))
print(next(it))


"""
REVISION NOTES

Iterable

nums = [1,2,3]

Iterator

it = iter(nums)

next(it)

returns next value

StopIteration

raised when values finish

For Loop

internally uses

iter()

next()

StopIteration

Iterator remembers position

Iterable does not
"""