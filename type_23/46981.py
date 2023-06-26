def f(x: int, y: int, was_multiply: bool) -> int:
    if x > y:
        return 0
    elif x == y:
        return 1
    if not was_multiply:
        return f(x + 1, y, False) + f(x + 2, y, False) + f(2 * x, y, True)
    else:
        return f(x + 1, y, False) + f(x + 2, y, False)


print(f(1, 11, False))
