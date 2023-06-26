for i in range(174457, 174505 + 1):
    count = 0
    dividers = []
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            count += 1
            dividers.append(j)
            if count > 2:
                break
    if count == 2:
        print(dividers)