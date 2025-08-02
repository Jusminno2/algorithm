N = int(input())
A = list(map(int, input().split()))

count = 0

for i in range(N):
    for j in range(i+1, N):
        if j - i == A[i-1] + A[j-1]:
            count += 1

print(count)