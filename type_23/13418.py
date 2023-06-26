def f(x: int, y: int) -> int:
    if x > y or x == 26:
        return 0
    elif x == y:
        return 1
    return f(x + 1, y) + f(2 * x + 1, y)


if __name__ == '__main__':
    print(f(1, 27))
