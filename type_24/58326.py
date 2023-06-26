with open("files/58326.txt", 'rt') as file:
    text = file.read()
max_count, count = 0, 0
for i in range(len(text) - 1):
    if int(text[i]) > int(text[i + 1]):
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1
print(max_count)