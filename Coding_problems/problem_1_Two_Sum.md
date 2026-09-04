# Two Sum

## Pattern
HashMap (Dictionary)

## Recognition
- Two numbers
- Target sum
- Return indices

## Approach
- Create a dictionary
- For each number, calculate `target - num`
- If complement exists, return indices
- Else store current number and index

## Code

```python
def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        needed = target - num

        if needed in seen:
            return [seen[needed], i]

        seen[num] = i
```

## Complexity

Time: O(n)
Space: O(n)

## Interview Tip

"Use a dictionary to store previously seen numbers and check whether the complement exists."