N, P, Q, R, S = map(int, input().split())
A = list(input().split())

A[P-1:Q], A[R-1:S] = A[R-1:S], A[P-1:Q]
print(" ".join(A))
