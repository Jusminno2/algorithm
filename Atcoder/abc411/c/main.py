"""
N = 0 ... 0 0 0 0 0
N = 1 ... 0 1 0 0 0
N = 2 ... 0 1 1 0 0
N = 3 ... 0 1 0 0 0
N = 4 ... 0 1 0 0 1
N = 5 ... 1 1 0 0 1
N = 6 ... 1 1 0 0 0
N = 7 ... 1 0 0 0 0
"""
from typing import List


def check_black(square: List[int], cache: List[List[int]]) -> int:
    """
    :param array: [1 1 0 0 1], [(1,1), (]
    :return: 3

    目的：
    - [1, 1, 0, 0, 1] から 1が連続する区間の数を効率良く見つけるための方法を探す

    注意：
    - 計算量の都合上、for 文は使用できない
    """
    pass


def main():
    N, Q = map(int, input().split())
    query = list(map(int, input().split()))

    square = [0] * N
    cache = list()

    for q in query:
        if square[q-1] == 0:
            square[q-1] = 1
        else:
            square[q-1] = 0


        ans = check_black(square, cache)
        print(ans)


if __name__ == '__main__':
    main()

