"""
工夫すべき点
・Node は２桁未満なので Node に注目していみる
・i-1 番目までの品物から価値がsum_vとなるように選んだときの重さの総和の最小値を dp[i][sum_v]とする
"""

INF = 1 << 60

# 入力
N, W = map(int, input().split())
w = [0] * N
v = [0] * N
for i in range(N):
    w[i], v[i] = map(int, input().split())

# 最大価値の総和を事前に計算（DPテーブルの横幅を決める）
max_v = sum(v)

# dp[i] := 価値 i を得るための最小の重さ
dp = [INF] * (max_v + 1)
dp[0] = 0  # 価値 0 は重さ 0 で達成できる

# DPループ
for i in range(N):
    for j in range(max_v, v[i] - 1, -1):  # 逆順にループ
        dp[j] = min(dp[j], dp[j - v[i]] + w[i])

# 出力：W以下の重さで実現可能な最大価値を探す
res = 0
for value in range(max_v + 1):
    if dp[value] <= W:
        res = value
print(res)

