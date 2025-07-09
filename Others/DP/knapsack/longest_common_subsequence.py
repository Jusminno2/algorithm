q = int(input())

for _ in range(q):
    X = input()
    Y = input()
    len_x = len(X)
    len_y = len(Y)

    """
    dp = [[0 for _ in range(len_x + 1)] for _ in range(len_y + 1)]
    """

    dp = [[0 for _ in range(len_y + 1)] for _ in range(len_x + 1)]

    for i in range(0, len_x+1):
        for j in range(0, len_y+1):
            if i >= 1 and j >= 1 and X[i-1] == Y[j-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + 1)
            elif i >= 1 and j >= 1:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            elif i >= 1:
                dp[i][j] = dp[i-1][j]
            elif j >= 1:
                dp[i][j] = dp[i][j-1]

    print(dp[len_x][len_y])