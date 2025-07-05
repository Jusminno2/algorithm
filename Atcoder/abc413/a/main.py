N, M = map(int, input().split())
A = list(map(int, input().split()))
sum_a = sum(A)

if sum_a <= M:
    print("Yes")
else:
    print("No")
