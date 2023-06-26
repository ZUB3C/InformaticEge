def mai_17(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        return mai_17(x + 1, y) + mai_17(x + 3, y)
print(mai_17(1, 8) * mai_17(8, 15))