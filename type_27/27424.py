# https://inf-ege.sdamgia.ru/problem?id=27424
with open("files/27424_B.txt", 'rt') as input_file:
    lines = input_file.read().split("\n")
n = lines[0]
del lines[0]
number_pairs = [tuple(map(int, i.split())) for i in lines if len(i) != 0]
min_delta = 10 ** 6
total_sum = 0

for a, b in number_pairs:
    total_sum += max(a, b)
    if abs(a - b) % 3 != 0:
        min_delta = min(min_delta, abs(a - b))
if total_sum % 3 != 0:
    print(total_sum)
else:
    print(total_sum - min_delta)
