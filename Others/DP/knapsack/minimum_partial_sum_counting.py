n = int(input())
a = list(map(int, input().split()))
A = int(input())

dp = [[10000000] * (A + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    for j in range(0, A + 1):
        if j >= a[i-1]:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j - a[i-1]] + 1)
        else:
            dp[i][j] = dp[i-1][j]

if dp[n][A] != 10000000:
    print(dp[n][A])
else:
    print(-1)