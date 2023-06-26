with open("files/47590.csv", 'rt') as file:
    data = [i for i in file.read().split("\n") if len(i) != 0]
d = {'0': 0}
for line in data:
    number, duration, *subprocesses = line.replace(';', ' ').replace(",", " ").split()
    d[number] = max([d[i] for i in subprocesses]) + int(duration)
print(max(d.values()))