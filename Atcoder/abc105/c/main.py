N = int(input())
A = [0 for _ in range(N)]
B = list(map(int, input().split()))

for i in range(N):
    if i == 0:
        A[i] = B[i]
        if N-1 == 1:
            A[i+1] = B[i]
        else:
            if B[i] < B[i + 1]:
                A[i + 1] = B[i]
            else:
                A[i + 1] = B[i + 1]

    elif 0 < i < N-1:
        if i == N-2:
            A[i+1] = B[i]
            break
        elif B[i] < B[i+1]:
            A[i+1] = B[i]
        else:
            A[i+1] = B[i+1]


print(sum(A))