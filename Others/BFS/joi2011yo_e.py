# 方針：S から 1、1 から 2、… と各ペア間を BFS で最短距離計算し合計
# 移動は 'X' 以外どこでも可能（工場を素通り可）。食べる時間は無視。

import sys
from collections import deque

def bfs(start, goal, grid, H, W):
    sr, sc = start
    gr, gc = goal
    if start == goal:
        return 0
    dist = [[-1]*W for _ in range(H)]
    q = deque()
    q.append((sr, sc))
    dist[sr][sc] = 0
    # 4近傍（北・南・西・東）
    for_pop = q.popleft  # 微最適化
    while q:
        r, c = for_pop()
        d = dist[r][c]
        # 上下左右
        nr = r - 1
        if nr >= 0 and grid[nr][c] != 'X' and dist[nr][c] == -1:
            if (nr, c) == (gr, gc):
                return d + 1
            dist[nr][c] = d + 1
            q.append((nr, c))
        nr = r + 1
        if nr < H and grid[nr][c] != 'X' and dist[nr][c] == -1:
            if (nr, c) == (gr, gc):
                return d + 1
            dist[nr][c] = d + 1
            q.append((nr, c))
        nc = c - 1
        if nc >= 0 and grid[r][nc] != 'X' and dist[r][nc] == -1:
            if (r, nc) == (gr, gc):
                return d + 1
            dist[r][nc] = d + 1
            q.append((r, nc))
        nc = c + 1
        if nc < W and grid[r][nc] != 'X' and dist[r][nc] == -1:
            if (r, nc) == (gr, gc):
                return d + 1
            dist[r][nc] = d + 1
            q.append((r, nc))
    # 到達保証があるためここには来ないはず
    return -1

def main():
    input = sys.stdin.readline
    H, W, N = map(int, input().split())
    grid = [list(input().strip()) for _ in range(H)]

    # 位置を収集：S と '1'..'N'
    pos = {}
    for i in range(H):
        for j in range(W):
            ch = grid[i][j]
            if ch == 'S' or ('1' <= ch <= '9'):
                pos[ch] = (i, j)

    total = 0
    cur = pos['S']
    for k in range(1, N+1):
        target = pos[str(k)]
        total += bfs(cur, target, grid, H, W)
        cur = target

    print(total)

if __name__ == "__main__":
    main()
