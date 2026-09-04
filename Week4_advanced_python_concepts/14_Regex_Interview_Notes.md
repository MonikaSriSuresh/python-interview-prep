# Python Regex Interview Notes

## Topics Covered

-   Character classes
-   Quantifiers
-   Anchors
-   Capturing, Named and Non-Capturing Groups
-   Alternation
-   Greedy vs Non-Greedy
-   re.search()
-   re.match()
-   re.fullmatch()
-   re.findall()
-   re.split()
-   re.sub()
-   re.compile()

## Quick Notes

### search vs match vs fullmatch

  Function    Purpose
  ----------- -----------------
  search      Search anywhere
  match       Beginning only
  fullmatch   Entire string

### Named Group

``` python
m = re.search(r"INV-(?P<number>\d+)", text)
m.group("number")
```

### Non-Capturing Group

``` python
(?:INV)
```

### Alternation

``` python
cat|cats
```

Left-to-right evaluation.

### Greedy

``` python
<.*>
```

### Non-Greedy

``` python
<.*?>
```

### findall

Returns all matches.

### split

Splits using regex delimiters.

### sub

``` python
re.sub(r"\d+","#","abc123xyz456")
# abc#xyz#
```

### compile

Compile once, reuse many times.

## Interview Questions

1.  search vs match vs fullmatch
2.  findall vs split
3.  Why compile?
4.  Greedy vs non-greedy
5.  Named vs non-capturing groups
6.  Difference between `\d a`{=tex}nd `\d+`{=tex}
7.  Real-world regex examples
