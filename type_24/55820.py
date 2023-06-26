with open("files/55820.txt", 'rt') as file:
    text = file.read()
max_count, count = 0, 0
for i in range(len(text) - 1):
    if text[i] not in 'QRS' or text[i + 1] not in 'QRS':
        count += 1
        max_count = max(max_count, count)
    # и text[i], и text[i + 1] в "QRS"
    else:
        count = 1
print(max_count)