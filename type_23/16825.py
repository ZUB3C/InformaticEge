def f(x: int, y: int) -> int:
    if x > y or x == 6 or x == 12:
        return 0
    elif x == y:
        return 1
    return f(x + 1, y) + f(2 * x, y) + f(x + 3, y)


if __name__ == '__main__':
    print(f(3, 16))
