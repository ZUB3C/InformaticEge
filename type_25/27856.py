for i in range(95_632, 95_650 + 1):
    odd_count = 0
    odd_dividers = []
    for j in range(1, i + 1, 2):
        if i % j == 0:
            odd_count += 1
            odd_dividers.append(j)
        if odd_count > 6:
            break
    if odd_count == 6:
        print(*odd_dividers)