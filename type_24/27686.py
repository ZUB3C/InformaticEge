with open('files/27686.txt', 'rt') as file:
    symbols = file.read()
current_len = 0
max_from_all_lens = 0
is_sequence = False
for symbol in symbols:
    if symbol == "X":
        current_len += 1
        # if not is_sequence:
        is_sequence = True
    else:
        if is_sequence:
            is_sequence = False
            max_from_all_lens = max(max_from_all_lens, current_len)
            current_len = 0
print(max_from_all_lens)

#  ИЛИ:
# print(max(map(len, open('files/27686.txt').readline().replace('Z', ' ').replace('Y', ' ').split())))