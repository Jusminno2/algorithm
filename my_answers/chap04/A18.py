# 入力
N, S = map(int, input().split())
A = list(map(int, input().split()))

# DP(i=0)
"""
0からスタートする理由：
・汎用性がなく設計が壊れるため=>dp[1][1]がスタートの場合、与えられた数によってdp[1][1]==Falseになってもらうと困る
    => どこがベースケースなのか読み手がわからなくなる
"""
dp = [[None] * (S+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(1, S+1):
    dp[0][i] = False

# DP(i=1)
for i in range(1, N+1):
    for j in range(0, S+1):
        if j < A[i-1]:
            if dp[i-1][j] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False

        if j >= A[i-1]:
            if dp[i-1][j] == True or dp[i-1][j-A[i-1]] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False

# Output
if dp[N][S] == True:
    print("Yes")
else:
    print("No")