"""
Input: "This is a pen. This is an apple. Applepen."
Output: {'p', 6}
"""
import operator
from typing import Tuple
from future.backports import Counter


# ネットで調べながら出した回答
def chars_counter(word):
    char_list = [char for char in word.split()]
    chars = ''.join(char_list)
    cache = {}

    for char in chars:
        cache[char] = cache.get(char, 0) + 1

    cache_sorted = sorted(cache.items(), key=lambda x: x[1], reverse=True)
    print(cache_sorted[0])


# 模範解答1
def count_chars_v1(strings: str) -> Tuple[str, int]:
    # 小文字に変更
    strings = strings.lower()
    """
    リスト内包括(この記述法だと毎回の文字についてカウントしてしまう)
    [('t', 2), ('h', 2), ('i', 4), ('s', 4), ('i', 4), ('s', 4), ('a', 4), ('p', 6), ('e', 4), ('n', 3), 
    ('.', 3), ('t', 2), ('h', 2), ('i', 4), ('s', 4), ('i', 4), ('s', 4), ('a', 4), ('n', 3), ('a', 4), 
    ('p', 6), ('p', 6), ('l', 2), ('e', 4), ('.', 3), ('a', 4), ('p', 6), ('p', 6), ('l', 2), ('e', 4), 
    ('p', 6), ('e', 4), ('n', 3), ('.', 3)]
    """
    l = [(c, strings.count(c)) for c in strings if not c.isspace()]

    return max(l, key=operator.itemgetter(1))


# 模範解答2
def count_chars_v2(strings: str) -> Tuple[str, int]:
    # 小文字に変更
    strings = strings.lower()
    d = dict()
    for char in strings:
        if not char.isspace():
            d[char] = d.get(char, 0) + 1    # はじめはゼロ
    max_key = max(d, key=d.get)
    return max_key, d[max_key]


# 模範解答3
def count_chars_v3(strings: str) -> Tuple[str, int]:
    # 小文字に変更
    strings = strings.lower()
    d = Counter()
    for char in strings:
        if not char.isspace():
            d[char] += 1
    max_key = max(d, key=d.get)
    return max_key, d[max_key]


if __name__ == '__main__':
    words = "This is a pen. This is an apple. Applepen."
    chars_counter(words)
    print(count_chars_v1(words))
    print(count_chars_v2(words))
    print(count_chars_v3(words))