simple = []
for i in range(2_422_000, 2_422_080 + 1):
    count = 0
    for j in range(2, i):
        if i % j == 0:
            count += 1
            break
    if count == 0:
        simple.append(i)
print("\n".join([f'{i + 1} {number}' for i, number in enumerate(simple)]))