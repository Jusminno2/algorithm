from collections import deque
from typing import List


# bfs 実装
def bfs(grid: List[int], R:int, C: int, sy: int, sx: int, gy: int, gx: int):
    seen = deque([[sy, sx]])
    dist = [[float("inf")] * C for _ in range(R)]
    dist[sy][sx] = 0

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while seen:
        p = seen.popleft()
        if p[0] == gy and p[1] == gx:
            break
        for i in range(4):
            ny, nx = p[0] + dy[i], p[1] + dx[i]
            if 0 <= nx < C and 0 <= ny < R and grid[ny][nx] != "#" and dist[ny][nx] == float("inf"):
                dist[ny][nx] = dist[p[0]][p[1]] + 1
                seen.append([ny, nx])

    return dist[gy][gx]

def main():
    R, C = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())

    grid = list()
    for _ in range(R):
        grid.append(input())

    # スタート地点
    sy = sy - 1
    sx = sx - 1
    # ゴール地点
    gy = gy - 1
    gx = gx - 1

    ans = bfs(grid, R, C, sy, sx, gy, gx)
    print(ans)


if __name__ == "__main__":
    main()


