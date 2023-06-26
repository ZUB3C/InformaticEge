with open('files/33199_B.txt', 'rt', encoding='utf-8') as f:
    data = [i for i in f.read().split('\n') if i]
n = data[0]
del data[0]
first_sum, second_sum, third_sum = 0, 0, 0
min_difference = 10 ** 30
for line in data:
    a, b, c = sorted(list(map(int, line.split())))
    first_sum += a
    second_sum += b
    third_sum += c
    if c - b < min_difference and b != c and (c - b) % 2 != 0 and (c - a) % 2 != 0:
        min_difference = c - b

if (first_sum % 2) == (second_sum % 2):
    print(third_sum - min_difference)
else:
    print(third_sum)