for i in range(125_256, 125_330 + 1):
    dividers = []
    count = 0
    for j in range(2, i + 1, 2):
        if i % j == 0:
            count += 1
            dividers.append(j)
            if count > 6:
                break
    if count == 6:
        print(*dividers)
