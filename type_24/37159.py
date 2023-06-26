with open("files/37159.txt", 'rt') as file:
    symbols = file.read()
max_len_from_all = 0
current_len = 0
for i in range(len(symbols)):
    if (symbols[i] == "a" and symbols[i + 1] == "d") or (symbols[i] == "d" and symbols[i + 1] == "a"):
        max_len_from_all = max(max_len_from_all, current_len)
        current_len = 1
    else:
        current_len += 1
print(max_len_from_all)