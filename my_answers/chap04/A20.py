# Input
S = input()
T = input()
N = len(S)
M = len(T)

# DP
dp = [[None] * (M+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(0, N+1):
    for j in range(0, M+1):
        # dp[0][0]以外 かつ 2つの文字が一致する 場合
        if i>=1 and j>=1 and S[i-1]==T[j-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + 1)
        # dp[0][0]以外の場合（文字は一致しない場合）
        elif i>=1 and j>=1:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # j = 0 の列について
        elif i>=1:
            dp[i][j] = dp[i-1][j]
        # i = 0 の列について
        elif j>=1:
            dp[i][j] = dp[i][j-1]


print(dp[N][M])