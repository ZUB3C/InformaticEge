#https://inf-ege.sdamgia.ru/problem?id=27991
with open('files/27991_B.txt', 'rt') as file:
    data = [i for i in file.read().split('\n') if len(i) != 0]
del data[0]
data = list(map(int, data))
pair = tuple()
max_sum = 0
was_good_pair = False
for i, a in enumerate(data):
    for b in data[i + 1:]:
        if (a - b) % 2 == 0 and ((a % 17 == 0) or (b % 17 == 0)):
            was_good_pair = True
            if (a + b) > max_sum:
                max_sum = a + b
                pair = (a, b)
if was_good_pair:
    print(*pair)
else:
    print(0, 0)