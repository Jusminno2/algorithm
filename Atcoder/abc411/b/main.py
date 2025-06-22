N = int(input())
D = list(map(int, input().split()))

for i in range(N):
    for j in range(i + 1, N-i):
        print(i+j)
