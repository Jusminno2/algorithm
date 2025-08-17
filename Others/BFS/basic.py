from collections import deque

N, M = map(int, input().split())    # N: 頂点数　M: 辺数
G = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    # 無向グラフのため両方に頂点を貼る
    G[A].append(B)
    G[B].append(A)

# 各頂点が何手目に探索されたか？ => 最短距離探索のため
# -1 は未探索
dist = [-1] * N

# todoリスト（今後読むべきサイト）を表すキューを召喚
queue = deque()

# 頂点 0 を始点とする
dist[0] = 0
# 読むべきリストに始点を追加
queue.append(0)

# キューが空になるまで探索する
# 初期状態でもキューに入っている
# その後キューがからになるということは全部見たということ
while queue:
    # キューから見るべきやつを取り出す（このあと、こいつのお隣さん入れていく）
    v = queue.popleft()

    # 頂点vのお隣さんをキューにぶち込む（探索済以外をキューにぶち込むのが仕事）
    for next_v in G[v]:
        # 探索済みかどうかチェック => 探索済みであれば何もしない
        if dist[next_v] != -1:
            continue

        # 頂点 next_v を探索する
        dist[next_v] = dist[v] + 1
        queue.append(next_v)