N, M = map(int, input().split())
S = [[0] for _ in range(M)]

# 含んでいるか判定するためのリスト
check = [int(i) for i in range(1, N+1)]

# 結果の計算
count = 0

# List S の形成
for i in range(M):
    _ = int(input())
    S[i] = list(map(int, input().split()))

for i in range(2 ** M):
    selected = list()
    for j in range(M):
        if ((i >> j) & 1):
            selected += S[j]
    # set にすることで部分集合との比較ができる
    if set(selected) >= set(check):
        count += 1

print(count)


