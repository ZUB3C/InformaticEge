with open("files/33196.txt", 'rt') as file:
    symbols = file.read()
data = {}
for i in range(0, len(symbols)):
    current_symbol = symbols[i]
    if current_symbol == "A":
        next_symbol = symbols[i + 1]
        if next_symbol not in data.keys():
            data[next_symbol] = 1
        else:
            data[next_symbol] += 1
max_count = 0
symbol = ""
for key, val in data.items():
    if val > max_count:
        max_count = val
        symbol = key
print(symbol)