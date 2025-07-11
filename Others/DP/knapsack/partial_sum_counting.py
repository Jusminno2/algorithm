n = int(input())
a = list(map(int, input().split()))
A = int(input())

dp = [[0] * (A+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(1, n+1):
    # 選ぶか選ばない決めれるから重さ0の場合もきちんと考慮する
    for j in range(0, A+1):
        if j >= a[i-1]:
            # 上から引き継ぐ場合と斜めからやって来る場合の総和やんか
            dp[i][j] = dp[i-1][j] + dp[i-1][j - a[i-1]]
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][A])