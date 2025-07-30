"""
並べ方は N! 通り
求める計算式は、すべての通りで計算した [表向き] / [通り数]
"""
import itertools
import math

N = int(input())
C = [int(input()) for _ in range(N)]
C = list(itertools.permutations(C))
# print(C)
count = 0


for c in C:
    reverse = [1 for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, N):
            if c[j] % c[i] == 0:
                if reverse[j] == 0:
                    reverse[j] = 1
                elif reverse[j] == 1:
                    reverse[j] = 0
    # print(f"{c}: {reverse}")
    count += sum(reverse)


ans = count / math.perm(N, N)
print(ans)

