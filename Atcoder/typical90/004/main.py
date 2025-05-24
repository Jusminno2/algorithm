h, w = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(h)]

ans = [[None] * w for _ in range(h)]
sum_row = 0
sum_col = 0

for i in range(h):
    for j in range(w):
        sum_row += array[i][j]
        sum_col += array[i][j]

