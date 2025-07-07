N, W = map(int, input().split())
v = [0] * N
w = [0] * N

for i in range(N):
    v[i], w[i] = map(int, input().split())

dp = [[0] * (W + 1) for _ in range(N + 1)]


"""
条件分岐
・i番目の商品を選んだ場合に重さが上限を超えない場合
    ・i番目の商品を選ぶ場合
    ・i番目の商品を選ばない場合
・i番目の商品を選んだ場合に重さが上限を超える場合
    ・i番目の商品は選べない
"""
for i in range(N):
    for j in range(W + 1):
        if j - w[i] >= 0:
            dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]] + v[i])
        else:
            dp[i+1][j] = dp[i][j]

print(dp[N][W])