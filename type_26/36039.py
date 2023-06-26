with open('files/36039.txt', 'rt', encoding='utf-8') as file:
    data = [i for i in file.read().split('\n') if len(i) != 0]
s, n = list(map(int, data[0].split()))
del data[0]
data = sorted(list(map(int, data)))
mass = 0
count = 0
for i, m in enumerate(data):
    if mass + m > s:
        max_index = i
        max_mass = m
        break
    mass += m
    count += 1

for i in data[max_index + 1:]:
    if mass - max_mass + i <= s:
        max_mass = i

print(count, max_mass)