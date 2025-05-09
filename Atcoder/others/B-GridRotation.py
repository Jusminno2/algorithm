def rotate(grid):
    # 90度右回転
    N = len(grid)
    return [''.join([grid[N - j - 1][i] for j in range(N)]) for i in range(N)]

def count_diff(grid1, grid2):
    # 異なるマスの数を数える
    N = len(grid1)
    return sum(1 for i in range(N) for j in range(N) if grid1[i][j] != grid2[i][j])

def min_operations(S, T):
    min_ops = float('inf')
    for rot in range(4):
        diff = count_diff(S, T)
        min_ops = min(min_ops, rot + diff)
        S = rotate(S)  # 次の回転
    return min_ops

# 入力処理
N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

# 出力
print(min_operations(S, T))
