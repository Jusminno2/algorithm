import heapq
from typing import List
from collections import Counter


def top_n_with_heap(words: List[str], n: int) -> List[int]:
    """
    wordsのカウント方法（No library）：
    d = {}
    for word in words:
        d[word] = d.get(word, 0) + 1

    であるが、pythonの標準ライブラリであるCounterを使うこともできる
    => 今回はCounterを用いる
    """
    counter_word = Counter(words)
    print(counter_word.most_common(n))

    # マイナスにすることで最も出現回数が多い数が上に来るようにしているこの部分がミソ
    data = [(-counter_word[word], word) for word in counter_word]
    heapq.heapify(data)
    print(data)

    return [heapq.heappop(data)[1] for _ in range(n)]


if __name__ == '__main__':
    words = ['python', 'c', 'java', 'go', 'python', 'c', 'go', 'python']
    print(top_n_with_heap(words, 3))
