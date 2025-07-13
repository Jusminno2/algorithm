N, L, R = map(int, input().split())
count = 0

for _ in range(N):
    x, y = map(int, input().split())
    if x <= L and y >= R:
        count += 1

print(count)
