from collections import deque

N, Q = map(int, input().split())
A = [int(i) for i in range(1, N + 1)]

def rotate(a,n):
    return a[n:] + a[:n]

for _ in range(Q):
    q = list(map(int, input().split()))

    # type1
    if q[0] == 1:
        p, x  = q[1], q[2]
        A[p-1] = x

    # type2
    elif q[0] == 2:
        p = q[1]
        print(A[p-1])

    # type3
    elif q[0] == 3:
        k = N - q[1] % N
        A = rotate(A, N-k)



