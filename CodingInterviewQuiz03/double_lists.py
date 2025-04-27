"""
Input   X: [1, 2, 3, 4, 5, 5, 8, 10]. Y: [4, 5, 5, 5, 6, 7, 8, 8, 10]
   =>   X: [1, 2, 3, 4, 4, 10].       Y: [5, 5, 5, 6, 7, 8, 8, 10]
"""

from typing import List, Counter
from collections import Counter


def min_count_remove(x: List[int], y: List[int]) -> None:
    count_x = {}
    count_y = {}
    for i in x:
        count_x[i] = count_x.get(i, 0) + 1
    for i in y:
        count_y[i] = count_y.get(i, 0) + 1

    # count_x = Counter(x)
    # count_y = Counter(y)

    for key_x, value_x in count_x.items():
        value_y = count_y.get(key_x)    # getを使わずcount_y[key_x]とすると、なかったときエラーが発生する
        if value_y:                     # getの場合はNoneが返ってくる
            if value_x < value_y:
                # x[:] を使っているのはこの関数はreturnしないから
                # return するなら話は変わってくる
                # ローカルスコープとグローバルスコープについて理解する必要あり
                x[:] = [i for i in x if i != key_x] # もともとのリストXに変更を加えたいからx[:]とした｜新しくリストを作り直してもよし！
            elif value_x > value_y:
                y[:] = [i for i in y if i != key_x]



if __name__ == '__main__':
    x = [1, 2, 3, 4, 4, 5, 5, 8, 10]
    y = [4, 5, 5, 5, 6, 7, 8, 8, 10]
    print('x = ', x)
    print('y = ', y)
    min_count_remove(x, y)
    print('x = ', x)
    print('y = ', y)