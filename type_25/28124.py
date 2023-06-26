# import time
# s = time.perf_counter()
number, final_count = 0, 0
for i in range(568_023, 569_230 + 1):
    count = 1  # Считаем само число своим делителем
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            count += 1
    if count > final_count:
        number = i
        final_count = count
    elif count == final_count:
        if i < number:
            number = i
            final_count = count
print(final_count, number)
# print(time.perf_counter() - s)