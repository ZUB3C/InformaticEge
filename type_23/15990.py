def f(x: int, y: int) -> int:
    if x > y:
        return 0
    elif x == y:
        return 1
    return f(x + 2, y) + f(x + 3, y) + f(x * 2, y)


if __name__ == '__main__':
    print(f(2, 11) * f(11, 22))