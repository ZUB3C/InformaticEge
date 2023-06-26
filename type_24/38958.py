with open("files/38958.txt", 'rt') as file:
    symbols = file.read()
max_from_all_lens, count, count_old = 0, 0, 0
for i in symbols:
    if i == "A":
        max_from_all_lens = max(max_from_all_lens, count + count_old + 1)
        count_old = count
        count = 0
    else:
        count += 1
max_from_all_lens = max(max_from_all_lens, count + count_old + 1)
print(max_from_all_lens)