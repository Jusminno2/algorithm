N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 配列の初期化
dp = [-(10 ** 9)] * (N+1)
dp[1] = 0

# DP
for i in range(1, N):
    dp[A[i-1]] = max(dp[A[i-1]], dp[i] + 100)
    dp[B[i-1]] = max(dp[B[i-1]], dp[i] + 150)

# 出力
print(dp[N])
