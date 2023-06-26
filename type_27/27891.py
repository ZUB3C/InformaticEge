# https://inf-ege.sdamgia.ru/problem?id=27891
with open('files/27891_B.txt', 'rt') as file:
    data = [i for i in file.read().split('\n') if len(i) != 0]
n = data[0]
del data[0]
data = list(map(int, data))
max_2, max_7, max_14, max_0 = 0, 0, 0, 0
for i in data:
    if i % 14 == 0:
        max_14 = max(max_14, i)
    elif i % 7 == 0:
        max_7 = max(max_7, i)
    elif i % 2 == 0:
        max_2 = max(max_2, i)
    else:
        max_0 = max(max_0, i)
x_number = max(max_14 * max(max_0, max_2, max_7), max_2 * max_7)
print(x_number)