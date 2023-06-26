for i in range(201_455, 201_470 + 1):
    count = 0
    dividers = []
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
            dividers.append(j)
        if count > 4:
            break
    if count == 4:
        print(*dividers)