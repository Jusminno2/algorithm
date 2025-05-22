s = input()
t = input()

dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
dp[0][0] = 0

for i in range(len(s) + 1):
    for j in range(len(t) + 1):
        if s[i-1] == t[j-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + 1)
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# LCSの復元
lcs = list()
i, j = len(s), len(t)

while i > 0 and j > 0:
    if s[i-1] == t[j-1]:
        lcs.append(s[i-1])
        i -= 1
        j -= 1
    # 上のマス ＞ 左のマス => 上のマス（dp）にジャンプ
    elif dp[i-1][j] > dp[i][j-1]:
        i -= 1
    # 左のマスにジャンプ
    else:
        j -= 1

lcs.reverse()
print(''.join(lcs))