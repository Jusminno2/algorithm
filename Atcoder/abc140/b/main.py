N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

res = 0

for i in range(N):
    if i < N-1:
        if A[i+1] - A[i] == 1:
            res += C[A[i]-1]

    res += B[A[i]-1]


print(res)
