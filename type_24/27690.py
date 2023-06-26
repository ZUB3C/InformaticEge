with open("files/27690.txt", 'rt') as file:
    symbols = file.read()
max_len_from_all = 0
current_len = 0
for i in range(1, len(symbols)):
    if symbols[i - 1] != symbols[i]:
        current_len += 1
    else:
        max_len_from_all = max(max_len_from_all, current_len)
        current_len = 1
print(max_len_from_all)