n = int(input())
K = int(input())
a = list(map(int, input().split()))
A = int(input())

dp = [[100000000] * (A+1) for _ in range(n+1)]
dp[0][0] = 0

"""
悩ましいポイント
・これまでは、min/maxで簡単に判断できていたが、今回はminでもなければmaxでもなさそう
・でも、「何通りあるのか」ではなくて「可能かどうか」の判定だからできそうかも
・最小で行ってみるか

教訓
・一般に bool 値を求める DP をすることは無駄であることが多く、同じ計算量でもっと多くのことを知ることができる
"""

for i in range(1, n + 1):
    for j in range(0, A + 1):
        if j >= a[i-1]:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j - a[i-1]] + 1)
        else:
            dp[i][j] = dp[i-1][j]

if dp[n][A] != 10000000 and dp[n][A] <= K:
    print("Yes")
else:
    print("No")