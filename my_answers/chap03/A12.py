from typing import List


def check(x: int, N: int, K: int, A: List[int]) -> bool:
    sum = 0
    for i in range(N):
        sum += x // A[i]    # ほしいのは整数値だけ

    if sum >= K:
        return True
    return False


# 入力
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 二分探索
Left = 1
Right = 10 ** 9

while Left <= Right:
    Mid = (Left + Right) // 2
    Answer = check(Mid, N, K, A)

    if Answer == False:
        Left = Mid + 1
    if Answer == True:
        Right = Mid - 1

# 出力
print(Left)