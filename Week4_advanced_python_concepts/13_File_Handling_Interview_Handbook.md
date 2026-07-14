# Topic 13 -- File Handling (Interview Handbook)

## Text vs Binary

-   Text: r, w, a
-   Binary: rb, wb, ab

## File Modes

-   r: Read
-   w: Write (truncate/create)
-   a: Append
-   r+, w+, a+
-   rb, wb

## Important Methods

-   read()
-   readline()
-   readlines()
-   write()
-   writelines()
-   seek()
-   tell()

Always prefer:

``` python
with open("file.txt") as f:
    ...
```

## JSON

-   dump(): Python object -\> JSON file
-   dumps(): Python object -\> JSON string
-   load(): JSON file -\> Python object
-   loads(): JSON string -\> Python object

## CSV

-   csv.reader()
-   csv.DictReader() (preferred)
-   csv.writer()

Always use:

``` python
open("employees.csv", "w", newline="")
```

## Pickle

-   pickle.dump()
-   pickle.load()

Use for Python-only serialization (ML models, caching).

Never unpickle untrusted data.

## Production Best Practices

-   Use `with`
-   Specify UTF-8 encoding
-   Stream large files
-   Use `dict.get()` for optional JSON fields
-   Use `json=` with requests
-   Add timeout and `raise_for_status()` for APIs
