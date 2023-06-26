for i in range(210_235, 210_300 + 1):
    count = 0
    dividers = []
    for j in range(2, i):
        if i % j == 0:
            count += 1
            dividers.append(j)
        if count > 4:
            break
    if count == 4:
        print(*dividers)