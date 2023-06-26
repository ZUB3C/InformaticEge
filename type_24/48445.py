with open("files/48445.txt", 'rt') as file:
    text = file.read()
sogl = "CDF"
gl = "AO"
step = 3
count, max_len = 0, 0
for i in range(0, len(text) - 1, step):
    if text[i] in sogl and text[i + 1] in sogl and text[i + 2] in gl:
        count += 1
        step = 3
        max_len = max(max_len, count)
    else:
        step = 2
        count = 0
print(max_len)