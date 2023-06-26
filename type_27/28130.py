#https://inf-ege.sdamgia.ru/problem?id=28130
with open('files/28130_B.txt', 'rt', encoding='utf-8') as f:
    numbers = f.read().split('\n')
numbers = list(map(int, numbers))
del numbers[0]

pair_count = 0
m = 80
c = 50
for i, a in enumerate(numbers):
    for b in numbers[i + 1:]:
        if (a + b) % m == 0 and ((a > c) or (b > c)):
            pair_count += 1
print(pair_count)

# Solution from sdamgia:

# start = time.perf_counter()
# k = 0
# for i in range(nums_count):
#     for j in range(i + 1, nums_count):
#         if (numbers[i] + numbers[j]) % 80 == 0 and (numbers[i] > 50 or numbers[j] > 50):
#             k = k + 1
#     i = i + 1
# print(k)
# print(time.perf_counter() - start)
