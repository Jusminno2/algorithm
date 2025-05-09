# Input
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

# 隣接リストの作成
G = [list() for _ in range(N+1)]    # G[i]は頂点iに隣接する頂点のリスト
for a, b in edges:
    G[a].append(b)  # 頂点aに隣接する頂点としてbを追加
    G[b].append(a)  # 頂点bに隣接する頂点としてaを追加

# 出力
for i in range(1, N+1):
    output = ''
    output += str(i)
    output += ': {'
    output += ', '.join(map(str, G[i]))
    output += '}'
    print(output)

"""
この実装では 頂点番号が1から始まる前提なので、
- G[0] はダミー（使わない）
- 1-indexedな構造に合わせて G を N+1 個確保しているだけ
"""