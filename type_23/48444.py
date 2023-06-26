def f(x: int, y: int) -> int:
    if x > y or "3" in str(x):
        return 0
    elif x == y:
        return 1
    return f(x + 1, y) + f(2 * x, y)


print(f(1, 40))
