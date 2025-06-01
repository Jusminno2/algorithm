N, M = map(int, input().split())
imos = [0] * (N+1)
for _ in range(M):
    l, r = map(int, input().split())
    l = l-1
    imos[l] += 1
    imos[r] -= 1
ans = 1e9
for i in range(1, N):
    imos[i] = imos[i-1] + imos[i]
    ans = min(ans, imos[i])

print(ans)