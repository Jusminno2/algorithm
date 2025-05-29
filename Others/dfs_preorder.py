# 深さ優先探索（行きがけ順）
from typing import List


def dfs(G: List[int], v: int, seen: List[int],
        pre_order: List[int], post_order: List[int]) -> None:
    seen[v] = True
    pre_order.append(v) # 行きがけ順=>訪れた順番にどんどん記載

    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(G, next_v, seen, pre_order, post_order)

    post_order.append(v)    # 隣接ノードがすべて訪問済みになったノードから格納していく


def main():

    N, M = map(int, input().split())

    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    seen = [False] * N
    pre_order = []
    post_order = []

    dfs(G, 0, seen, pre_order, post_order)

    print("行きがけ順：")
    for v in pre_order:
        print(v)

    print("帰りかけ順：")
    for v in post_order:
        print(v)


if __name__ == "__main__":
    main()