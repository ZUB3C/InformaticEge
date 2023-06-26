with open('files/36000.txt', 'rt', encoding='utf-8') as file:
    data = [i for i in file.read().split('\n') if len(i) != 0]
n = int(data[0])
del data[0]
data = list(map(int, data))
pair_count, max_middle = 0, 0
s = set(data)
for i, a in enumerate(data):
    for j, b in enumerate(data[i + 1:]):
        if (a + b) % 2 == 1:
            if a + b in s:
                pair_count += 1
                max_middle = max(max_middle, a + b)
print(pair_count, max_middle)