n, m = map(int, input().split())
coins = list(map(int, input().split()))

dp = [[1000000 for _ in range(n+1)] for _ in range(m+1)]
dp[0][0] = 0

# Point1 => iのrangeをどうするか？ => i番目のコインを選ぶかどうかで考えたい（商品をコインに置換する） => iはコインindexであるmで表す
for i in range(1, m+1):
    for j in range(n+1):
        # Point2 => 0円もあり得るから、0スタート
        # Point3 => コインのindex調整 => coins[i-1]とする
        # Point4 => 比較対象を考える（1: i-1番目までのコインを用いてj円にするコイン枚数の最小値からなにもコインを選ばない
        #                          2: i番目までのコインを用いてj円にするために、同じコインを使用する
        #                          3: i-1番目の状態から、i番目のコインを使用してj円にする）
        if j >= coins[i-1]:
            dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]] + 1, dp[i-1][j-coins[i-1]] + 1)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[m][n])