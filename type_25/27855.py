for i in range(95_632, 95_700 + 1):
    even_count = 0
    even_dividers = []
    for j in range(2, i + 1, 2):
        if i % j == 0:
            even_count += 1
            even_dividers.append(j)
        if even_count > 6:
            break
    if even_count == 6:
        print(*even_dividers)