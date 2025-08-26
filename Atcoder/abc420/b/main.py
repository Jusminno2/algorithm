n, m = map(int, input().split())
S = [input() for _ in range(n)]

# m 回の結果を入れる配列
win = [None for _ in range(m)]
points = [0 for _ in range(n)]

for i in range(m):
    count_x = 0
    count_y = 0
    for s in S:
        if s[i] == '0':
            count_x += 1
        elif s[i] == '1':
            count_y += 1
    if count_x == n or count_y == n:
        win[i] = None
    elif count_x < count_y:
        win[i] = '0'
    elif count_y < count_x:
        win[i] = '1'


for i in range(n):
    for j in range(m):
        if win[j] is None:
            continue
        else:
            if win[j] == S[i][j]:
                points[i] += 1

max_point = max(points)
max_id = ([i+1 for i, _ in enumerate(points) if points[i] == max_point])
print(' '.join(map(str, max_id)))



