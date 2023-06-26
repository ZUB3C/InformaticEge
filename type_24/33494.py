with open("files/33196.txt", 'rt') as file:
    symbols = file.read()
max_count = 0
symbol = ""
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if symbols.count("E" + letter) > max_count:
        max_count = symbols.count("E" + letter)
        symbol = letter
print(symbol)