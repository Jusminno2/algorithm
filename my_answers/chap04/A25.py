H, W = map(int, input().split())
HW = [[j for j in input().split()] for _ in range(H)]

# 配列の初期化
dp = [[0 for _ in range(W+1)] for _ in range(H+1)]

# dp
for i in range(1, H+1):
    for j in range(1, W+1):
        if HW[i-1][j-1] == "#":
            dp[i][j] = 0
        elif i == 1 and j ==1:
            dp[i][j] = 1
        else:
            if i >= 2:
                dp[i][j] += dp[i-1][j]
            # 両方から挟めるからifを使う
            if j >= 2:
                dp[i][j] += dp[i][j-1]

# for i in range(H):
#     for j in range(W):
#         if i == 0 and j == 0:
#             dp[i][j] = 1
#         else:
#             dp[i][j] = 0
#             if i>=1 and HW[i-1][j]=='.':
#                 dp[i][j] += dp[i-1][j]
#             if j>=1 and HW[i][j-1]=='.':
#                 dp[i][j] += dp[i][j-1]

print(dp)
print(dp[H][W])