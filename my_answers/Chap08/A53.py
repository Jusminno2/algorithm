import heapq

# 入力
Q = int(input())
queries = [input().split() for _ in range(Q)]

# クエリの処理
T = []
for q in queries:
    if q[0] == "1":
        heapq.heappush(T, int(q[1]))
    if q[0] == "2":
        print(T[0]) # T[0]は「優先度付きキューの最小要素」となっている
    if q[0] == "3":
        heapq.heappop(T)

"""
注意 1：Python の heapq モジュールは、deque モジュールとは異なり、関数を使って list を操作するという形式
注意 2：優先度付きキューの最小要素は T[0] で取り出せますが、例えば小さいほうから 2 番目の要素が T[1] で取り出せるとは限らない
注意 3：heapとはなにか、理解して使う必要がある
"""