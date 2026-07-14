# Topic 12 - Modules & Packages

## What is a Module?

- A module is a single Python (.py) file.
- It contains related functions, classes and variables.
- Modules improve code reusability and organization.

Example:

```python
# math_utils.py

def add(a, b):
    return a + b
```

```python
import math_utils

print(math_utils.add(10, 20))
```

---

## Advantages of Modules

- Code Reusability
- Better Organization
- Easier Maintenance
- Avoid Duplicate Code
- Namespace Separation

---

## Import Styles

### Import Entire Module

```python
import math

print(math.sqrt(25))
```

### Import Specific Function

```python
from math import sqrt

print(sqrt(25))
```

### Import Multiple Functions

```python
from math import sqrt, factorial
```

### Import with Alias

```python
import numpy as np
import pandas as pd
```

### Wildcard Import

```python
from math import *
```

❌ Not recommended due to namespace pollution.

---

## __name__

Every module has a special variable:

```python
__name__
```

### Executed Directly

```python
python demo.py
```

```
__name__ == "__main__"
```

### Imported

```python
import demo
```

```
__name__ == "demo"
```

---

## if __name__ == "__main__"

Used to execute code only when the file is run directly.

```python
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(10, 20))
```

Benefits:

- Prevents test code from running during import.
- Separates reusable code from executable code.

---

## Package

A package is a folder containing related Python modules.

Example:

```
calculator/

    add.py
    subtract.py
```

---

## Subpackage

Packages can contain other packages.

```
company/

    employee/

    finance/
```

---

## __init__.py

Special file executed when a package is imported.

Uses:

- Package initialization
- Expose selected functions
- Create a clean public API

Example:

```python
from .add import add
```

Allows:

```python
from calculator import add
```

instead of

```python
from calculator.add import add
```

---

## Absolute Import

Starts from the top-level package.

```python
from company.employee.developer import code
```

Preferred in large projects.

---

## Relative Import

Uses dot notation.

```python
from .developer import code
```

```
.   -> Current package

..  -> Parent package
```

Useful within the same package.

---

## sys.path

Python searches modules using:

```python
import sys

print(sys.path)
```

Search Order:

1. Current Directory
2. sys.path
3. Standard Library
4. Installed Packages

---

## Module Shadowing

Avoid naming files:

```
math.py
json.py
random.py
os.py
typing.py
```

Python imports the current directory first, hiding built-in modules.

---

## Circular Import

Occurs when two modules import each other.

```
a.py

    imports b.py

b.py

    imports a.py
```

Avoid by:

- Refactoring code
- Using a common module
- Importing inside functions

---

## Best Practices

✅ Use absolute imports in large projects

✅ Use relative imports within the same package

✅ Keep imports at the top

✅ Use aliases

```python
import numpy as np
import pandas as pd
```

❌ Avoid

```python
from module import *
```

❌ Don't shadow built-in module names.

---

# Interview Questions

1. What is a module?

2. What is a package?

3. Difference between module and package?

4. How does import work internally?

5. Explain __name__.

6. Why use if __name__ == "__main__"?

7. Difference between absolute and relative imports?

8. What is __init__.py?

9. What is sys.path?

10. What is circular import?

11. Why shouldn't we name a file math.py?

12. Difference between:

- import math
- from math import sqrt

13. AttributeError vs TypeError during imports.

14. What is module shadowing?

15. Explain Python's module search order.

---

# Quick Revision

Module = Single .py file

Package = Folder containing modules

__name__ = Module name

__main__ = File executed directly

__init__.py = Package initialization

Absolute Import = Starts from top package

Relative Import = Uses dot notation

sys.path = Module search path

Avoid wildcard imports

Avoid module shadowing

Avoid circular imports