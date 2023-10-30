from math import sqrt


def factorization(n: int):
    i = 2

    sqrt_from_n = round(sqrt(n))

    while i <= sqrt_from_n:
        if n % i == 0:
            count = 0
            while n % i == 0:
                count += 1
                n //= i
            yield i, count
            sqrt_from_n = round(sqrt(n))
        i += 1
    if n > 1:
        yield n, 1


if __name__ == '__main__':
    n = 24
    res = []
    for factor, power in factorization(n):
        res.append(f"{factor}^{power}")
    print('*'.join(res))
