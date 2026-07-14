"""
==========================================
Topic 12 : Modules & Packages
Interview Revision
==========================================
"""

# ==========================================
# 1. Import Entire Module
# ==========================================

import math

print(math.sqrt(25))
print(math.pi)

# ==========================================
# 2. Import Specific Function
# ==========================================

from math import sqrt

print(sqrt(16))

# ==========================================
# 3. Import Multiple Functions
# ==========================================

from math import factorial

print(factorial(5))

# ==========================================
# 4. Import Alias
# ==========================================

import math as m

print(m.sqrt(36))

# ==========================================
# 5. __name__
# ==========================================

print(__name__)

# ==========================================
# 6. if __name__ == "__main__"
# ==========================================

def add(a, b):
    return a + b


if __name__ == "__main__":
    print(add(10, 20))

# ==========================================
# 7. Package Example
# ==========================================

# calculator/
#
#     __init__.py
#     add.py
#     subtract.py

# from calculator import add
# from calculator.add import add

# ==========================================
# 8. Relative Import
# ==========================================

# from .developer import code
# from ..finance.salary import calculate_salary

# ==========================================
# 9. Absolute Import
# ==========================================

# from company.employee.developer import code

# ==========================================
# 10. sys.path
# ==========================================

import sys

print(sys.path)

# ==========================================
# 11. Module Shadowing (Avoid)
# ==========================================

# Bad Examples

# math = 100
# list = []
# str = "Hello"
# json = {}

# ==========================================
# 12. Circular Import Example
# ==========================================

# a.py
#
# from b import hello

# b.py
#
# from a import hi

# Causes Circular Import

# ==========================================
# 13. Best Practices
# ==========================================

# ✔ Prefer absolute imports
# ✔ Use relative imports within same package
# ✔ Keep imports at top
# ✔ Use aliases when appropriate
# ✔ Avoid wildcard imports
# ✔ Avoid naming files:
#    math.py
#    json.py
#    os.py
#    random.py

# ==========================================
# End of Topic 12
# ==========================================