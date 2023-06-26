def f(x: int, y: int) -> int:
    if x > y:
        return 0
    elif x == y:
        return 1
    return f(x + 3, y) + f(x + 4, y) + f(x + 5, y)


print(f(22, 42))
