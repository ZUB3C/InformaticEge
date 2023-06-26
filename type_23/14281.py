def f(x: int, y: int) -> int:
    if x > y:
        return 0
    elif x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y)


print(f(1, 11))
