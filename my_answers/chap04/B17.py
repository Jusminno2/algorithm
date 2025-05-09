N = int(input())
h = list(map(int, input().split()))

# 配列を初期化
dp = [10**6]*N

# dp
dp[0] = 0
for i in range(1, N):
    if i == 1:
        dp[i] = abs(h[i] - h[i-1])
    else:
        dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), dp[i-2] + abs(h[i-2] - h[i]))

Answer = []
Place = N-1

while True:
    Answer.append(Place)
    if Place == 0:
        break
    if dp[Place-1] + abs(h[Place]-h[Place-1]) == dp[Place]:
        Place -= 1
    else:
        Place -= 2

Answer.reverse()
for i in range(len(Answer)):
    Answer[i] += 1

print(len(Answer))
# Joinメソッドの対象は文字列だけ
print(" ".join(map(str, Answer)))