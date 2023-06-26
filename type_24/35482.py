with open("files/35482.txt", 'rt') as file:
    words = [i for i in file.read().split('\n') if len(i) != 0]
# data = {i: i.count("G") for i in words}
# needed_str = min(data, key=lambda x: data[x])
needed_str = min(words, key=lambda x: x.count("G"))
print(max(needed_str, key=lambda x: needed_str.count(x)))