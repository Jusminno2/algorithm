s = input()
t = input()

len_s = len(s)
len_t = len(t)

dp = [[0] * (len_t + 1) for _ in range(len_s + 1)]

for i in range(1, len_s + 1):
    for j in range(1, len_t + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + 1)
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

ans = list()

i = len_s
j = len_t

while i >= 1 and j >= 1:
    if s[i-1] == t[j-1]:    # 現在の文字が一致していると意味
        ans.append(s[i-1])
        i = i - 1
        j = j - 1
    elif max(dp[i-1][j], dp[i][j-1]) == dp[i - 1][j]:
        i = i - 1
    elif max(dp[i-1][j], dp[i][j-1]) == dp[i][j-1]:
        j = j - 1

ans.reverse()
print("".join(ans))