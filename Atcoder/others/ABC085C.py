N, Y = map(int, input().split())

for i in range(N+1):
    for j in range(N+1-i):
        k = N - i - j
        rest = 1000 * k

        if Y - 10000*i - 5000*j == rest:
            print(i, j, k)
            exit()

print(-1, -1, -1)


