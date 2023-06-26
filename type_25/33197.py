for i in range(1_000_000, 2_000_000 + 1):
    count = 0
    for j in range(round(i ** 0.5), 1000, -1):
        if i % j == 0:
            if abs(i // j - j) <= 100:
                count += 1
        if count == 3:
            print(i)
            break