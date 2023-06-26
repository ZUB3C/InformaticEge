# https://inf-ege.sdamgia.ru/problem?id=27990
import time
from pathlib import Path
import os


def main(path_to_file: str | Path) -> int:
    with open(file=path_to_file, mode='rt', encoding='utf-8') as input_file:
        lines = input_file.read().split("\n")
    n = lines[0]
    number_pairs = [tuple(map(int, i.split())) for i in lines[1:] if len(i) != 0]
    min_delta = 10 ** 6
    total_sum = 0
    for x, y in number_pairs:
        total_sum += max(x, y)
        if abs(x - y) % 5 != 0:
            min_delta = min(abs(x - y), min_delta)
    if total_sum % 5 != 0:
        return total_sum
    else:
        return total_sum - min_delta


if __name__ == '__main__':
    start_time = time.perf_counter()
    path_to_file = os.path.join(Path(__file__).parent, 'files/27990_B.txt')
    result = main(path_to_file)
    print(result)
    print(time.perf_counter() - start_time)
