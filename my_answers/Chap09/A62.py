import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)

# 深さ優先探索を行う関数（pos: 現在位置、visited[x]: 頂点 x が青色かどうかを表す真偽値）
def dfs(pos, G, visited):
    visited[pos] = True
    # i を起点とした i と隣接する頂点全てに色塗りを行う
    for i in G[pos]:
        if visited[i] == False:
            dfs(i, G, visited)

# 入力
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

# 隣接リスト
G = [list() for i in range(N+1)]    # G[i]: 頂点 i に隣接する頂点のリスト
for a, b in edges:
    G[a].append(b)  # 頂点 a に隣接する頂点として b を追加
    G[b].append(a)  # 頂点 b に隣接する頂点として a を追加

# 深さ優先探索
visited = [False for _ in range(N+1)]
dfs(1, G, visited)

# 連結かどうかの判定（answer = true のとき連結）
answer = True
for i in range(1, N+1):
    if visited[i] == False:
        answer = False

# 答えの出力
if answer == True:
    print("The graph is connected.")
else:
    print("The graph is not connected.")