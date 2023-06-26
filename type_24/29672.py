with open("files/29672.txt", 'rt') as file:
    lines = file.read().split("\n")
print(sum([1 for i in lines if i.count("E") > i.count("A")]))