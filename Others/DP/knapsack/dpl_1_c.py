N, W  = map(int, input().split())
v = [0 for _ in range(N)]
w = [0 for _ in range(N)]

for i in range(N):
    v[i], w[i] = map(int, input().split())

dp = [[0] * (W+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(W+1):
        if j-w[i-1] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1], dp[i][j-w[i-1]] + v[i-1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][W])