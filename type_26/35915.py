with open('files/35915.txt', 'rt', encoding='utf-8') as file:
    data = [i for i in file.read().split('\n') if len(i) != 0]
n = int(data[0])
del data[0]
data = list(map(int, data))
pair_count, max_middle = 0, 0
odd_data = list(filter(lambda x: x % 2 == 1, data))
s = set(data)
for i, a in enumerate(odd_data):
    for j, b in enumerate(odd_data[i + 1:]):
        middle = (a + b) // 2
        if a % 2 == 1 and b % 2 == 1:
            if middle in s:
                pair_count += 1
                max_middle = max(max_middle, middle)
print(pair_count, max_middle)