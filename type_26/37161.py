with open('files/37161.txt', 'rt', encoding='utf-8') as file:
    data = [i for i in file.read().split('\n') if len(i) != 0]
n = int(data[0])
del data[0]
data = [tuple(map(int, line.split())) for line in data]
pairs = sorted([(a, - b) for a, b in data])
max_row_number, min_sit_number = 0, 0
for i in range(1, len(pairs)):
    if pairs[i][0] == pairs[i - 1][0]:
        if pairs[i][1] - pairs[i - 1][1] == 3:
            max_row_number = pairs[i][0]
            min_sit_number = 1 - pairs[i][1]
print(max_row_number, min_sit_number)