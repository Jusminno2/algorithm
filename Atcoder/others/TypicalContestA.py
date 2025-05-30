dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

H, W  = map(int, input().split())
field = [input() for _ in range(H)]
print(field)

# seen[h][w] -> マス h, w が検知済みかどうか
seen = [[False] * W for _ in range(H)]
print(seen)

def dfs(h, w):
    seen[h][w] = True

    # 四方を探索
    for dir in range(4):
        nh = h + dx[dir]
        nw = w + dy[dir]

        # 場外アウトや移動先が壁の場合はスルー
        # indexがゼロより小さい or indexが壁を表す場所の場合
        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            continue
        if field[nh][nw] == '#':    # 進もうとしている先のマスが'#'なら進めない
            continue
        if seen[nh][nw]:    # 進もうとしている先のマスが検知済みであれば進まない
            continue

        # すべてをクリアしたもののみ...
        dfs(nh, nw)


for h in range(H):
    for w in range(W):
        if field[h][w] == 's':
            sh, sw = h, w
        if field[h][w] == 'g':
            gh, gw = h, w


# 探索開始
dfs(sh, sw)


if seen[gh][gw]:
    print('Yes')
else:
    print('No')