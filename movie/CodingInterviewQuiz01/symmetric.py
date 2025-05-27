"""
Symmetric
Input [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
Output [(5, 3), (7, 4)]

問題分析：
ペアを探せ => キャッシュとかハッシュテーブルを効果的に使う

yield関数について：
・リストや辞書などを総称してイテレーター（反復可能オブジェクト）と呼ぶ
・イテレーターは、あらかじめ用意された要素をforループで取り出す。

・これに対し、ジェネレーターは、イテレーターと同じ反復処理なのだが、要素を取り出すときにその都度要素を生成する。
・返り値はジェネレータオブジェクトとなる
"""

from typing import List, Iterator, Tuple


def find_pair(pairs: List[Tuple[int, int]]) -> Iterator[Tuple[int, int]]:
    cache = {}
    for pair in pairs:
        first, second = pair[0], pair[1]
        value = cache.get(second)
        if not value:
            cache[first] = second
        elif value == first:
            yield pair


if __name__ == "__main__":
    l = [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
    print(find_pair(l))
    for r in find_pair(l):
        print(r)
