#https://inf-ege.sdamgia.ru/problem?id=29675
with open('files/29675_B.txt', 'rt', encoding='utf-8') as f:
    data = f.read().split('\n')
n = data[0]
del data[0]

total_sum = 0
delta_list = []
for line in data:
    a, b = map(int, line.split())
    total_sum += max(a, b)
    if abs(a - b) % 3 != 0:
        delta_list.append(abs(a - b))
if total_sum % 3 == 0:
    print(total_sum)
else:
    delta_list.sort()
    i = 0
    k = 0
    while total_sum % 3 != 0:
        if total_sum % 3 != 0:
            if (total_sum - delta_list[i]) % 3 == 0:
                total_sum = total_sum - delta_list[i]
                print(total_sum)
                break
            else:
                i += 1
        if k < 1:
            if (total_sum - (delta_list[0] + delta_list[1])) % 3 == 0:
                total_sum = total_sum - (delta_list[0] + delta_list[1])
                print(total_sum)
                break
            else:
                k += 1
        i += 1
#  Explanation here: https://inf-ege.sdamgia.ru/problem?id=29675