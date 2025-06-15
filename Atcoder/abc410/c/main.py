from collections import deque

N, Q = map(int, input().split())
A = [int(i) for i in range(1, N + 1)]

offset = 0

for _ in range(Q):
    q = list(map(int, input().split()))

    # type1
    if q[0] == 1:
        p, x  = q[1]-1, q[2]
        A[(p + offset) % N] = x

    # type2
    elif q[0] == 2:
        p = q[1] -1
        print(A[(p + offset) % N])

    # type3
    elif q[0] == 3:
        k = q[1]
        offset = (offset + k) % N





