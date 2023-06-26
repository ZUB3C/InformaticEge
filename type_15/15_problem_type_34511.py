for A in range(0, 32):
    b = True
    for x in range(0, 32):
        if ((x & 25 == 0) or (x & 19 != 0) or (x & A != 0)) == 0:
            b = False
    if b:
        print(A)
        break
