with open("files/47228.txt", 'rt') as file:
    text = file.read()
sogl = "CDF"
gl = "AO"
step = 2
count, max_len = 0, 0
for i in range(0, len(text), step):
    if text[i] in sogl and text[i + 1] in gl:
        count += 1
        step = 2
        max_len = max(max_len, count)
    else:
        step = 1
        count = 0
print(max_len)