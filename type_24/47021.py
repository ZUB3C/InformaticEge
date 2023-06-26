with open("files/47021.txt", 'rt') as file:
    text = file.read()
print(len(list(filter(lambda x: len(x) >= 8 and "B" not in x, text.split("A")))))