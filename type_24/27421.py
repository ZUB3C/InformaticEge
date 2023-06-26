# https://inf-ege.sdamgia.ru/problem?id=27421
with open("files/27421.txt", 'rt') as file:
    symbols = file.read()
len_of_current_not_repeating_sequence = 1
max_from_all_lens = 0
for i in range(1, len(symbols)):
    if symbols[i - 1] != symbols[i]:
        len_of_current_not_repeating_sequence += 1
    else:
        max_from_all_lens = max(max_from_all_lens, len_of_current_not_repeating_sequence)
        len_of_current_not_repeating_sequence = 1
max_from_all_lens = max(max_from_all_lens, len_of_current_not_repeating_sequence)
print(max_from_all_lens)