# https://inf-ege.sdamgia.ru/problem?id=33106
with open('files/33106_A.txt', 'rt', encoding='utf-8') as f:
    data = [i for i in f.read().split('\n') if i]
n = data[0]
del data[0]

total_sum = 0
#  Так как числа в паре не превышают 10000:
dif1 = 20001  # Разница между числами в паре, дающая остаток 1 при делении на 3
dif2 = 20001  # Предыдущая разница между числами в паре, дающая остаток 1 при делении на 3
dif3 = 20001  # Разница между числами в паре, дающая остаток 2 при делении на 3
dif4 = 20001  # Предыдущая разница между числами в паре, дающая остаток 2 при делении на 3

for line in data:
    a, b = map(int, line.split())
    total_sum += min(a, b)
    dif_module = abs(a - b)
    if dif_module % 3 != 1 and dif_module < dif1:
        dif2 = dif1
        dif1 = dif_module
    elif dif_module % 3 != 1 and dif_module < dif2:
        dif2 = dif_module
    elif dif_module % 3 != 2 and dif_module < dif3:
        dif4 = dif3
        dif3 = dif_module
    elif dif_module % 3 != 2 and dif_module < dif4:
        dif4 = dif_module

# print(dif1)
# print(dif2)
# print(dif3)
# print(dif4)
# print(total_sum % 3)
# print()
if total_sum % 3 == 0:
    print(total_sum)
elif total_sum % 3 == 1:
    if (total_sum + dif3) < (total_sum + dif1 + dif2):
        print(total_sum + dif3)
    else:
        print(total_sum + dif1 + dif2)
elif total_sum % 3 == 2:
    if ((total_sum + dif1) < (total_sum + dif3 + dif4)):
        print(total_sum + dif1)
    else:
        print(total_sum + dif3 + dif4)
