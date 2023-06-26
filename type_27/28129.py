#https://inf-ege.sdamgia.ru/problem?id=28129
with open('files/28129_B.txt', 'rt') as file:
    data = [i for i in file.read().split('\n') if len(i) != 0]
del data[0]
data = list(map(int, data))
pair = tuple()
max_sum = 0
was_good_pair = False
d = 160
p = 7
for i, a in enumerate(data):
    for b in data[i + 1:]:
        if (a - b) % d != 0 and ((a % p == 0) or (b % p == 0)):
            was_good_pair = True
            if (a + b) > max_sum:
                max_sum = a + b
                pair = (a, b)
if was_good_pair:
    print(*pair)
else:
    print(0, 0)