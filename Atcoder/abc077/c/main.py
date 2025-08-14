import bisect

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

res = 0

for i in range(N):
    Aj = bisect.bisect_left(A, B[i])
    Cj = N - bisect.bisect_right(C, B[i])
    res += Aj * Cj

print(res)