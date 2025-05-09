# input
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Dynamic Programming
dp = [None] * (N+1)
dp[1] = 0
dp[2] = A[0]

for i in range(3, N+1):
    dp[i] = min(dp[i-1]+A[i-2], dp[i-2]+B[i-3])

# 答えの復元
# 変数 Place は現在の位置を表す
# 入力例の場合、Place は 5->4->3->2->1 と変化する
Answer = []
Place = N
while True:
    # Place は最後尾からスタートし、条件によって1つ戻るのか2つ戻るのかが決まる
    # はじめは、無条件にAppendしても良い
    Answer.append(Place)
    if Place == 1:
        break

    # どこから Place に向かうのが最適かを求める
    if dp[Place-1] + A[Place-2] == dp[Place]:
        Place = Place - 1
    else:
        Place = Place - 2

Answer.reverse()

Answer2 = [str(i) for i in Answer]
print(len(Answer))
print(' '.join(Answer2))