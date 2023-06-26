from math import sqrt, ceil


def is_simple(n: int) -> bool:
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for i, num in enumerate(range(245_690, 245_756 + 1)):
    if is_simple(num):
        print(i + 1, num)
