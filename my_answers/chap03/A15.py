import bisect

# input
N = int(input())
A = list(map(int, input().split()))

# 重複を消した配列Tの作成
T = list(set(A))
T.sort()

# 答えを求める
B = [None] * N
for i in range(N):
    B[i] = bisect.bisect_left(T, A[i])
    # 1からスタートするように+1する
    B[i] += 1

# 答えを空白区切りで出力
Answer = [str(i) for i in B]
print(' '.join(Answer))

# # 各値にランク（順位）を割り振る辞書を作成
# rank = {}
# for i, value in enumerate(T):
#     rank[value] = i + 1  # 1から始まるランク（0から始めたい場合は +1 を外す）
#
# # ランクに置き換えたリストを作成
# B = [rank[x] for x in A]
#
# # 出力
# print(' '.join(map(str, B)))