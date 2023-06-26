for i in range(110_203, 110_245 + 1):
    even_count = 0
    even_dividers = []
    for j in range(2, i + 1, 2):
        if i % j == 0:
            even_count += 1
            even_dividers.append(j)
        if even_count > 4:
            break
    if even_count == 4:
        print(*even_dividers)