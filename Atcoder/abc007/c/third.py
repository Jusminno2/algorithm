from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

grid = [input() for _ in range(r)]

# グリッド特有の移動の簡易化のために...
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# todoリストの作成
que = deque()
que.append((sy-1, sx-1))

# 距離
dist = [[-1 for _ in range(c)] for _ in range(r)]
# 初期条件
dist[sy-1][sx-1] = 0

while que:
    v, u = que.popleft()
    for i in range(4):
        next_v = v + dy[i]
        next_u = u + dx[i]
        if 0 <= next_v <= r-1 and 0 <= next_u <= c-1:
            if grid[next_v][next_u] == '#':
                continue
            elif grid[next_v][next_u] == '.':
                if dist[next_v][next_u] != -1:
                    continue
                dist[next_v][next_u] = dist[v][u] + 1
                que.append((next_v, next_u))

# print(dist)
print(dist[gy-1][gx-1])