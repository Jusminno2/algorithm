N = int(input())
H = list(map(int, input().split()))

# dp[j] は 足場 j に行くときの最小コストを表す
dp = [None] * (N+1)
dp[0] = 0
dp[1] = 0

for j in range(2, N+1):
    if j == 2:
        dp[j] = dp[j-1] + abs(H[j-1] - H[j-2])
    elif j > 2:
        dp[j] = min(dp[j-1] + abs(H[j-1] - H[j-2]), dp[j-2] + abs(H[j-1] - H[j-3]))

print(dp[N])

