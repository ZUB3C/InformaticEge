# https://inf-ege.sdamgia.ru/problem?id=27989
import os
from pathlib import Path


path_to_file = os.path.join(Path(__file__).parent, 'files/27989_B.txt')
with open(path_to_file, mode='rt') as file:
    lines = file.read().split("\n")
n = lines[0]
del lines[0]
numbers = list(map(int, lines))

n_0, n_2, n_13, n_26 = 0, 0, 0, 0

for i in numbers:
    if i % 26 == 0:
        n_26 += 1
    elif i % 13 == 0:
        n_13 += 1
    elif i % 2 == 0:
        n_2 += 1
    else:
        n_0 += 1
result = n_26 * n_0 + n_13 * n_2 + n_13 * n_26 + n_2 * n_26 + n_26 * (n_26 - 1) // 2
print(result)
