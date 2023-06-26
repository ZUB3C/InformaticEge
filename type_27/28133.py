#https://inf-ege.sdamgia.ru/problem?id=28133
with open('files/28133_B.txt', 'rt', encoding='utf-8') as f:
    data = f.read().split('\n')
data = list(map(int, data))
n = data[0]
del data[0]
pair = tuple()
max_sum = 0
was_good_pair = False
m = 120
for i, a in enumerate(data):
    for j, b in enumerate(data[i + 1:]):
        if a > b and i < j <= n and (a + b) % m == 0:
            was_good_pair = True
            if a + b > max_sum:
                max_sum = a + b
                pair = (a, b)
if was_good_pair:
    print(*pair)
else:
    print("00")
