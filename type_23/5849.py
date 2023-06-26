def f(x: int, y: int) -> int:
    if x > y:
        return 0
    elif x == y:
        return 1
    return f(x + 1, y) + f(x + 10, y)  # так как числа меньше 100


print(f(35, 57))
