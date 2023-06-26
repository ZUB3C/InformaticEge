for i in range(312_614, 312_651 + 1):
    count = 0
    dividers = []
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
            dividers.append(j)
        if count > 6:
            break
    if count == 6:
        print(*dividers)