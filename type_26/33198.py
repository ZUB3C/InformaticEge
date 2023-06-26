with open('files/33198.txt', 'rt', encoding='utf-8') as file:
    weights = [i for i in file.read().split('\n') if len(i) != 0]
n, m = map(int, weights[0].split())
del weights[0]
weights = sorted(list(map(int, weights)))
count, total_weight = 0, 0
d = []
for i in weights:
    if 200 <= i <= 210:
        count += 1
        total_weight += i
    else:
        d.append(i)
d.sort()

d2 = []
i = 0

while sum(d2) + d[i] <= m - total_weight:
    count += 1
    d2.append(d[i])
    i += 1
k = len(d) - 1

while i > 0:
    while k >= 0:
        if sum(d2) - d2[i-1] + d[k] <= m - total_weight and d[k] != 0:
            d2[i-1] = d[k]
            d[k] = 0
            i -= 1
            break
        else:
            k -= 1
total_weight += sum(d2)
print(count, total_weight)