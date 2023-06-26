for i in range(185_311, 185_330 + 1):
    s = []
    divider_count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            divider_count += 1
            s.append(j)
            if divider_count > 4:
                break
    if divider_count == 4:
        print(*s)
