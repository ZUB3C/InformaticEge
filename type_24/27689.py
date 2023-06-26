import re
f = open('files/27689.txt').read()
r = re.findall(r'(?:XYZ)+(?:XY|X)?', f)
r = map(len, r)
print(max(r))