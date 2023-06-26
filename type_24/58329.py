with open("files/58329.txt", 'rt') as file:
    text = file.read()
max_count, count = 0, 0
for i in range(len(text) - 2):
    if int(text[i]) + int(text[i + 1]) > int(text[i + 2]):
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1
print(max_count)