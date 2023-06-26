import re
with open("files/27699.txt", "rt") as file:
    symbols = file.read()
r = re.findall(r"(?:LDR)+(?:L|LD)?", symbols)
print(max(map(len, r)))