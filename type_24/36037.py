with open("files/36037.txt", 'rt') as file:
    symbols = file.read()
max_sequence_len = 0
current_char_sequence = ''
for symbol in symbols:
    current_char_sequence += symbol
    if "XZZY" in current_char_sequence:
        max_sequence_len = max(max_sequence_len, len(current_char_sequence) - 1)
        current_char_sequence = ''
print(max_sequence_len + 3)  # Так как надо посчитать "XZZ" в подстроке
