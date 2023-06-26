with open("files/33103.txt", 'rt') as file:
    lines = file.read().split("\n")
print(sum([1 for i in lines if i.count("A") > i.count("E")]))