def dfs(G, v, seen):
    seen[v] = True

    # v から行ける next_v について
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(G, next_v, seen)


def main():

    N, M, s, t = map(int, input().split())

    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    # 頂点 s をスタートとした探索
    seen = [False] * N
    dfs(G, s, seen)

    # t にたどり着けるかどうか
    if seen[t]:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()