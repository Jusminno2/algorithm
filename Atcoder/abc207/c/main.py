N = int(input())
t = [-1 for _ in range(N)]
l = [-1 for _ in range(N)]
r = [-1 for _ in range(N)]
for i in range(N):
    t[i], l[i], r[i] = map(int, input().split())

ans = 0

for i in range(N):
    for j in range(i + 1, N):
        if t[i] == 1:
            pass
        elif t[i] == 2:
            pass
        elif t[i] == 3:
            pass
        elif t[i] == 4:
            pass

