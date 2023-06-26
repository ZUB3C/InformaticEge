with open("files/40999.txt", 'rt') as file:
    text = file.read()
print(max(map(len, filter(lambda x: x.count("A") >= 3, text.split("E")))))