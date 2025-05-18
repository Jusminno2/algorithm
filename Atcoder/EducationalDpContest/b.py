N, K = map(int, input().split())
H = list(map(int, input().split()))

dp = [float('inf')] * N
dp[0] = 0

# dp[0] => 足場1を表す
for i in range(N):
    for j in range(1, K+1):
        # i は起点　j はジャンプ先（具体例：i=0,j=1 のとき、dp[0+1]=dp[1]への配り方を考える）
        if i + j < N:
            # 配る遷移方式
            dp[i+j] = min(dp[i+j], dp[i] + abs(H[i] - H[i+j]))


print(dp[N-1])