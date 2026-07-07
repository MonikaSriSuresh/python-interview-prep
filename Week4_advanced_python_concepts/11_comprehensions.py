"""
==========================================================
Topic 11 - Comprehensions
==========================================================
"""

print("=" * 60)
print("1. Basic List Comprehension")
print("=" * 60)

numbers = [x for x in range(5)]
print(numbers)

# Equivalent Loop
numbers = []

for x in range(5):
    numbers.append(x)

print(numbers)


print("\n" + "=" * 60)
print("2. Expression in List Comprehension")
print("=" * 60)

squares = [x * x for x in range(5)]
print(squares)


print("\n" + "=" * 60)
print("3. Filtering")
print("=" * 60)

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

# Equivalent Loop

result = []

for x in range(10):
    if x % 2 == 0:
        result.append(x)

print(result)


print("\n" + "=" * 60)
print("4. Conditional Expression")
print("=" * 60)

result = [x if x % 2 == 0 else -x for x in range(6)]
print(result)

# Equivalent Loop

result = []

for x in range(6):

    if x % 2 == 0:
        result.append(x)

    else:
        result.append(-x)

print(result)


print("\n" + "=" * 60)
print("5. Nested List Comprehension")
print("=" * 60)

matrix = [
    [1, 2],
    [3, 4]
]

flatten = [j for i in matrix for j in i]
print(flatten)

# Equivalent Loop

result = []

for i in matrix:

    for j in i:

        result.append(j)

print(result)


print("\n" + "=" * 60)
print("6. Dictionary Comprehension")
print("=" * 60)

square_dict = {x: x * x for x in range(6)}
print(square_dict)

# Equivalent Loop

result = {}

for x in range(6):
    result[x] = x * x

print(result)


print("\n" + "=" * 60)
print("7. Dictionary Example")
print("=" * 60)

names = ["Anand", "Rahul", "John"]

length = {name: len(name) for name in names}

print(length)


print("\n" + "=" * 60)
print("8. Dictionary with if-else")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]

result = {
    x: "Even" if x % 2 == 0 else "Odd"
    for x in numbers
}

print(result)


print("\n" + "=" * 60)
print("9. Set Comprehension")
print("=" * 60)

numbers = [1, 2, 2, 3, 3, 4, 4, 5]

unique = {x for x in numbers}

print(unique)

# Equivalent Loop

result = set()

for x in numbers:
    result.add(x)

print(result)


print("\n" + "=" * 60)
print("10. Set Filtering")
print("=" * 60)

result = {x * x for x in range(10) if x % 2 == 0}

print(result)


print("\n" + "=" * 60)
print("11. Generator Expression")
print("=" * 60)

g = (x for x in range(5))

print(type(g))


print("\n" + "=" * 60)
print("12. next() with Generator")
print("=" * 60)

g = (x for x in range(3))

print(next(g))
print(next(g))
print(next(g))


print("\n" + "=" * 60)
print("13. Generator inside for Loop")
print("=" * 60)

g = (x for x in range(5))

for value in g:
    print(value)


print("\n" + "=" * 60)
print("14. Generator to Tuple")
print("=" * 60)

g = (x for x in range(5))

t = tuple(g)

print(t)


print("\n" + "=" * 60)
print("15. Generator to List")
print("=" * 60)

g = (x for x in range(5))

lst = list(g)

print(lst)


print("\n" + "=" * 60)
print("16. List vs Generator")
print("=" * 60)

list_comp = [x for x in range(10)]

gen_exp = (x for x in range(10))

print(type(list_comp))
print(type(gen_exp))


print("\n" + "=" * 60)
print("17. Interview Example")
print("=" * 60)

numbers = [1, 2, 3, 4]

result = [x * 10 if x % 2 == 0 else x for x in numbers]

print(result)


print("\n" + "=" * 60)
print("18. Interview Example")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]

result = [x * x for x in numbers if x > 2]

print(result)


print("\n" + "=" * 60)
print("19. Interview Example")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]

result = {
    x: x * x
    for x in numbers
    if x % 2 == 0
}

print(result)


print("\n" + "=" * 60)
print("20. Interview Example")
print("=" * 60)

numbers = [1, 2, 2, 3, 3, 4]

result = {x for x in numbers}

print(result)


print("\n" + "=" * 60)
print("21. Important Notes")
print("=" * 60)

print("List Comprehension      -> []")
print("Dictionary Comprehension-> {}")
print("Set Comprehension       -> {}")
print("Generator Expression    -> ()")

print("\nGenerator is memory efficient.")
print("List stores all values in memory.")
print("Set automatically removes duplicates.")
print("Dictionary stores key-value pairs.")
print("There is NO Tuple Comprehension in Python.")