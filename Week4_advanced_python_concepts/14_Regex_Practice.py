import re

print(re.search(r"INV-(?P<number>\d+)", "Invoice INV-1001").group("number"))
print(re.match(r"Hello","Hello Python"))
print(re.fullmatch(r"\d+","12345"))
print(re.findall(r"\d+","Age 25 Marks 98"))
print(re.split(r"[,;]","apple,banana;orange"))
print(re.sub(r"\d+","#","abc123xyz456"))

pattern = re.compile(r"\d+")
print(pattern.findall("Age 25"))
print(pattern.findall("Marks 98"))
