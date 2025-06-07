import sys

"""
- 再帰上限がデフォルトで 1000 なので変更する
- 1 << 20 はビットシフト演算子で 2 の 20 乗 => 1048576
- シフト演算子の記述必要
"""
sys.setrecursionlimit(1 << 20)

# 入力
N, M = map(int, input().split())

"""
グラフの初期化を行う
・ g[a] = b => 頂点aは頂点bに隣接する　※ a は index=0 からスタートすることに注意
"""
g = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())    # 隣接する2頂点を取得
    A -= 1
    B -= 1
    g[A].append(B)
    g[B].append(A)

# DFS
visited = [False] * (N+1)   # なぜ N+1 なのか？
path = []

def dfs(i: int) -> None:
    path.append(i)

    # ゴール地点にたどり着いた場合...
    if i == N - 1:
        # 答えを出力して終了
        for x in path:
            print(x + 1)    # index のズレを調整
        exit(0)

    # その他の場合...
    visited[i] = True

    for j in g[i]:
        if not visited[j]:
            dfs(j)
    path.pop()

dfs(0)