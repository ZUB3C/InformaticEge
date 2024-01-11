# https://inf-ege.sdamgia.ru/problem?id=27415
import csv
from typing import List, Tuple


def find_max_min_coins_route(matrix: List[List[int]]) -> Tuple[int, int]:
    n = len(matrix)

    max_dp = [[0] * n for _ in range(n)]
    min_dp = [[0] * n for _ in range(n)]

    # Заполняем первую строку и первый столбец матриц
    for i in range(n):
        max_dp[0][i] = min_dp[0][i] = sum(matrix[0][:i + 1])
        max_dp[i][0] = min_dp[i][0] = sum(row[0] for row in matrix[:i + 1])

    for i in range(1, n):
        for j in range(1, n):
            max_dp[i][j] = matrix[i][j] + max(max_dp[i - 1][j], max_dp[i][j - 1])
            min_dp[i][j] = matrix[i][j] + min(min_dp[i - 1][j], min_dp[i][j - 1])

    return max_dp[n - 1][n - 1], min_dp[n - 1][n - 1]


matrix = []
with open("files/27415.csv", 'rt') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        matrix.append(list(map(int, row)))

max_coins, min_coins = find_max_min_coins_route(matrix)
print(f"{max_coins}{min_coins}")
