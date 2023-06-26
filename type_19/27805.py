def f(x: int, move: int) -> bool:
    # Нет третьего хода, так как игра заканчивается на втором по условию.
    # Вместо него подводиться итог - победил ли второй игрок, или нет.
    if move == 3:
        if x >= 63:
            return True
        else:
            return False
    else:
        return f(x + 1, move + 1) or f(x + 4, move + 1) or f(x * 5, move + 1)


for s in range(1, 62 + 1):
    if f(s, 1):
        print(s)
        break
