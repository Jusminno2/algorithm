"""
Python には、heapqというheapのpushやpop、リストのヒープ化を行ってくれる標準ライブラリが存在する。
具体的には、以下の種類がある。（https://docs.python.org/ja/3.13/library/heapq.html）
・heapq.heappush(heap, item)
・heapq.heappop(heap) ⋯ pop を行い、 heap から最小の要素を返します。ヒープ不変式は保たれます。
　　　　　　　　　　　　　　ヒープが空の場合、 IndexError が送出されます。
・heapq.heapify(x)  ⋯ リスト x をインプレース処理し、線形時間でヒープに変換
・heapq.nlargest(n, iterable, key=None)
・heapq.nsmallest(n, iterable, key=None)
"""

import heapq

numbers = [1,3,2,5,4,7,9,6,0,8]
heap_data = []

heapq.heapify(numbers)
print(numbers)
print(heapq.nlargest(3, numbers))
print(heapq.nsmallest(3, numbers))

for num in numbers:
    heapq.heappush(heap_data, num)

print(heap_data)

while heap_data:
    print(heapq.heappop(heap_data))