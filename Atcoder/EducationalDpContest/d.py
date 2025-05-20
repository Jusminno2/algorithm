N, W = map(int, input().split())
w = [0] * N
v = [0] * N

for i in range(N):
    w[i], v[i] = map(int, input().split())

dp = [[0] * (W+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
    for j in range(0, W+1):
        if j < w[i]:
            dp[i][j] = dp[i-1][j]
        if j >= w[i]:
            # すべてのジャンプではなく、ジャンプできるところからジャンプする
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])

print(max(dp[N]))
