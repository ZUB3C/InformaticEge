def f(x, y):
    if x > y or x == 5 or x == 10:
        return 0
    elif x == y:
        return 1
    else:
        return f(x + 1, y) + f(2 * x, y) + f(x + 3, y)

print(f(2, 14))