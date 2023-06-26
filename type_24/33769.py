with open("files/33769.txt", 'rt') as file:
    text = file.read()
data = {}
for i in range(len(text) - 2):
    if text[i] == text[i + 1]:
        current_letter = text[i + 2]
        if current_letter not in data.keys():
            data[current_letter] = 1
        else:
            data[current_letter] += 1
print(max(data, key=lambda x: data[x]))