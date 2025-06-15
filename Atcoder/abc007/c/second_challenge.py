from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
# Point1 => 0-index とすること！
sy = sy-1
sx = sx-1
gy, gx = map(int, input().split())
gy = gy-1
gx = gx-1

G = [input() for _ in range(R)]

# Point2 => 決まった移動についてはデータ構造で保持しておくと記述が楽！
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

# Point3 => 明らかに未到達とわかる数値で初期化をすること！
dist = [[-1] * C for _ in range(R)]
# Point4 => スタート地点を0とすること！[0][0]ではないよ！
dist[sy][sx] = 0
# データの持ち方大事かも！
q = deque([(sy, sx)])

while q:
    ly, lx = q.popleft()
    for i in range(4):
        ty, tx = ly + dy[i], lx + dx[i]
        # Point5 => ここの条件分岐がマジで大事！特に、幅のチェックと未到達チェック
        if 0 <= ty < R and 0 <= tx < C and G[ty][tx] == "." and dist[ty][tx] == -1:
            dist[ty][tx] = dist[ly][lx] + 1
            q.append((ty, tx))

print(dist[gy][gx])

