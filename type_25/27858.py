number, final_count = [], 0
for i in range(120_115, 120_200 + 1):
    count = 0
    dividers = []
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
            dividers.append(j)
    if count > final_count:
        final_count = len(dividers)
        number = i
    elif count == final_count:
        if i > number:
            final_count = len(dividers)
print(final_count, number)