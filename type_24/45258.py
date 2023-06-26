# With regex
import re
with open("files/45258.txt", 'rt') as file:
    text = file.read()
r = re.findall(r"(?:AB|CB)+", text)
print(max(map(len, r)) // 2)

# A normal person's solution
with open("files/45258.txt", 'rt') as file:
    text = file.read()
text = text.replace("AB", "L").replace("CB", "L")\
    .replace("A", " ").replace("B", " ").replace("C", " ").strip().split()
print(max(map(len, text)))
