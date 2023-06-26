ans = []
for A in range(0, 300):
    k = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if (4 * x + 3 * y < A) or (x >= y) or (y >= 13):
                k += 1
    if k == 300 ** 2:
        ans.append(A)
        print(A)
    k = 0

print(ans)
print(len(ans))
print(min(ans))
