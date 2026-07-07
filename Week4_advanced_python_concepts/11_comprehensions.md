# Topic 11 - Comprehensions

## What are Comprehensions?

Comprehensions provide a concise and Pythonic way to create collections (List, Dictionary, Set) or Generator objects from an iterable.

Instead of writing multiple lines using loops, comprehensions allow the same logic in a single readable statement.

---

# Why use Comprehensions?

- Less code
- More readable
- Pythonic
- Slightly faster than traditional loops
- Easy to apply transformations and filtering

---

# Types of Comprehensions

1. List Comprehension
2. Dictionary Comprehension
3. Set Comprehension
4. Generator Expression

---

# List Comprehension

## Syntax

```python
[expression for item in iterable]
```

Example

```python
numbers = [x for x in range(5)]
```

Output

```python
[0, 1, 2, 3, 4]
```

Equivalent Loop

```python
numbers = []

for x in range(5):
    numbers.append(x)
```

---

# Expression

```python
[x*x for x in range(5)]
```

Output

```python
[0,1,4,9,16]
```

---

# Filtering

```python
[x for x in range(10) if x % 2 == 0]
```

Output

```python
[0,2,4,6,8]
```

Only elements satisfying the condition are added.

---

# Conditional Expression

```python
[x if x % 2 == 0 else -x for x in range(5)]
```

Output

```python
[0,-1,2,-3,4]
```

Every element is processed.

---

# Nested List Comprehension

```python
matrix = [[1,2],[3,4]]

result = [j for i in matrix for j in i]
```

Output

```python
[1,2,3,4]
```

Equivalent Loop

```python
result = []

for i in matrix:
    for j in i:
        result.append(j)
```

---

# Dictionary Comprehension

## Syntax

```python
{key:value for item in iterable}
```

Example

```python
{x:x*x for x in range(5)}
```

Output

```python
{
0:0,
1:1,
2:4,
3:9,
4:16
}
```

---

Another Example

```python
names=["Anand","Rahul","John"]

{name:len(name) for name in names}
```

Output

```python
{
'Anand':5,
'Rahul':5,
'John':4
}
```

---

# Set Comprehension

## Syntax

```python
{expression for item in iterable}
```

Example

```python
{x for x in [1,2,2,3,3,4]}
```

Output

```python
{1,2,3,4}
```

Sets automatically remove duplicate values.

---

# Generator Expression

## Syntax

```python
(expression for item in iterable)
```

Example

```python
g = (x for x in range(5))
```

Type

```python
<class 'generator'>
```

Generator Expressions generate values lazily (one at a time).

---

Example

```python
g=(x for x in range(3))

print(next(g))
print(next(g))
print(next(g))
```

Output

```python
0
1
2
```

The generator remembers where it stopped after every `next()` call.

---

# Generator vs List Comprehension

List Comprehension

```python
[x for x in range(1000000)]
```

- Creates entire list
- Higher memory usage
- Faster random access

Generator Expression

```python
(x for x in range(1000000))
```

- Creates generator object
- Generates one value at a time
- Memory efficient
- Uses lazy evaluation

---

# Equivalent Loops

List

```python
result=[]

for x in numbers:
    result.append(x)
```

Dictionary

```python
result={}

for x in numbers:
    result[x]=x*x
```

Set

```python
result=set()

for x in numbers:
    result.add(x)
```

Generator

```python
def generator():
    for x in numbers:
        yield x
```

---

# Common Interview Questions

### Why are comprehensions preferred?

- More readable
- Pythonic
- Less code
- Slightly faster

---

### Difference between filtering and conditional expression?

Filtering

```python
[x for x in numbers if x>5]
```

Only matching elements are added.

Conditional Expression

```python
[x if x>5 else 0 for x in numbers]
```

Every element is added.

---

### Difference between List and Generator?

| List | Generator |
|------|-----------|
| Stores everything | Generates one at a time |
| High Memory | Low Memory |
| Uses append() | Uses yield() internally |
| Faster indexing | No indexing |

---

### Why does Set use add() instead of append()?

Because sets do not maintain order like lists and store only unique values.

---

### Is there a Tuple Comprehension?

No.

```python
(x for x in range(5))
```

creates a Generator Expression, not a tuple.

To create a tuple

```python
tuple(x for x in range(5))
```

---

# Common Mistakes

❌ Forgetting that filtering and conditional expressions are different.

❌ Using list comprehension when generator is sufficient.

❌ Thinking `(x for x in nums)` creates a tuple.

❌ Using `append()` on a set.

❌ Treating loop variable as an index.

---

# Quick Revision

List

```python
[x for x in nums]
```

Dictionary

```python
{x:x*x for x in nums}
```

Set

```python
{x for x in nums}
```

Generator

```python
(x for x in nums)
```

---

# Interview Tips

✅ Prefer comprehensions when creating a new collection.

✅ Use Generator Expressions for large datasets.

✅ Remember:
- List → append()
- Set → add()
- Dictionary → key:value
- Generator → lazy evaluation

---

# Summary

- Comprehensions are concise and Pythonic.
- List comprehensions create lists.
- Dictionary comprehensions create key-value pairs.
- Set comprehensions remove duplicates automatically.
- Generator expressions are memory efficient and generate values lazily.
- There is no tuple comprehension in Python.