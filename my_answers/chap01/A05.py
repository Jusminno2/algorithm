N, K = map(int, input().split())

result = 0

# 3重ループはO(N^3)だからあかん
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if i + j + k == K:
                result += 1

# 2重ループ全探索
for i in range(1, N+1):
    for j in range(1, N+1):
        z = K -i - j
        if z >= 1 and z <= N:
            result += 1


print(result)
