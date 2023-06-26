for i in range(2_000_000, 3_000_000 + 1):
    count = 0
    # for j in range(round(i ** 0.5), 1, -1):
    for j in range(1, round(i ** 0.5) + 1):
        if i % j == 0:
            if abs(i // j - j) <= 115:
                count += 1
        if count == 3:
            print(i)
            break