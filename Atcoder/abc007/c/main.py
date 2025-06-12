from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

maze = [input() for _ in range(R)]
print(maze)
sy -= 1
sx -= 1
gy -= 1
gx -= 1
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

q = deque([(sy, sx)])
dist = [[-1] * C for _ in range(R)]
dist[sy][sx] = 0

while q:
    y, x = q.popleft()
    for i in range(4):
        ay = y + dy[i]
        ax = x + dx[i]
        if 0 <= ay < R and 0 <= ax < C and maze[ay][ax] == '.' and dist[ay][ax] == -1:
            dist[ay][ax] = dist[y][x] + 1
            q.append((ay, ax))

print(dist[gy][gx])

