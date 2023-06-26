with open("files/57431.txt", 'rt') as file:
    text = file.read()
max_count, count = 0, 0
for i in range(len(text) - 1):
    if text[i] not in 'ABC' or text[i + 1] not in 'ABC':
        count += 1
        max_count = max(max_count, count)
    # Else выполняется <=> и text[i], и text[i + 1] в "ABC"
    else:
        count = 1
print(max_count)