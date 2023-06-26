#https://inf-ege.sdamgia.ru/problem?id=28131
with open('files/28130_B.txt', 'rt', encoding='utf-8') as f:
    data = f.read().split('\n')
data = list(map(int, data))
del data[0]
pair = tuple()
max_sum = 0
was_good_pair = False
m = 120
for i, a in enumerate(data):
    for j, b in enumerate(data[i + 1:]):
        if i < j and a > b and (a + b) % m == 0:
            was_good_pair = True
            if a + b > max_sum:
                max_sum = a + b
                pair = (a, b)
if was_good_pair:
    print(*pair)
else:
    print(0, 0)