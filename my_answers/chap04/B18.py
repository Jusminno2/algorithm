N, S = map(int, input().split())
A = list(map(int, input().split()))

# 配列を初期化
dp = [[None for _ in range(S+1)] for j in range(N+1)]
dp[0][0] = True
for i in range(1, S+1):
    dp[0][i] = False

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


if dp[N][S] == True:
    Answer_idx = []
    for i in reversed(range(N+1)):
        for j in reversed(range(S+1)):
            if i == N and j == S:
                Answer_idx.append(i)
            elif dp[i - 1][j - A[i - 1]] == True:
                Answer_idx.append(i)
    print(Answer_idx)




