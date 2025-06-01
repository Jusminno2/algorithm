n, m = map(int, input().split())
imos = [0] * (n+1)
for _ in range(m):
    l, r = map(int, input().split())
    l -= 1
    imos[l] += 1
    imos[r] -= 1    # rはr+1のところにしたいから大丈夫！
for i in range(1, n+1): # 実際は2からだけどindexの都合上1からになる
    imos[i] += imos[i-1]
ans = 1e9   # 1 * 10**9
for i in range(n):  # 0で初期化しているから0の場合も対応可能
    ans = min(ans, imos[i])
print(ans)
