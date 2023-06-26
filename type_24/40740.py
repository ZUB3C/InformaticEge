with open("files/40740.txt", 'rt') as file:
    text = file.read()
s = list(filter(lambda x: x.count("E") >= 3, text.split('A')))
print(max(map(len, s)))