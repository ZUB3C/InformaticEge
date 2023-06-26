with open("files/46982.txt", 'rt') as file:
    text = file.read()
text = text.split('E')
print(len(list(filter(lambda x: len(x) >= 10 and "F" not in x, text))))