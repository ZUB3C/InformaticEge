import re
with open("files/27694.txt", 'rt') as file:
    symbols = file.read()
r = re.findall(r"(?:AB)+(?:A)?", symbols)
print(max(map(len, r)))