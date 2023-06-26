# Explanation: https://ru.stackoverflow.com/questions/1501327/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC-%D0%BF%D0%B5%D1%80%D0%B5%D0%B1%D0%BE%D1%80%D0%B0-%D1%87%D0%B8%D1%81%D0%B5%D0%BB

m = 2
while True:
    n = m ** 4
    if n > 389_123_456:
        break
    if n >= 289_123_456:
        if all(m % i != 0 for i in range(2, m)):  # <=> m is prime?
            print(n, m ** 3)
    m += 1

# Slower solution:
for i in range(289_123_456, 389_123_456 + 1):
    sqrt_from_i = i ** 0.5
    count = 0
    if round(sqrt_from_i) == sqrt_from_i:
        biggest_divider = 1
        for j in range(2, round(sqrt_from_i) - 1):
            if i % j == 0:
                if biggest_divider == 1:
                    biggest_divider = i // j
                count += 2
        if count == 2:
            print(i, biggest_divider)
