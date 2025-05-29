# 深さ優先探索（行きがけ順）
from typing import List


def dfs(G: List[int], v: int, seen: List[int],
        in_time: List[int], out_time: List[int], time: List[int]) -> None:
    seen[v] = True
    in_time[v] = time[0]
    time[0] += 1  # 行きがけ順=>訪れた順番にどんどん記載

    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(G, next_v, seen, in_time, out_time, time)

    out_time[v] = time[0]
    time[0] += 1    # 隣接ノードがすべて訪問済みになったノードから格納していく


def main():

    N, M = map(int, input().split())

    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    seen = [False] * N
    in_time = [-1] * N
    out_time = [-1] * N
    time = [0]

    dfs(G, 0, seen, in_time, out_time, time)

    print("ノードの訪問と終了時刻：")
    for v in range(N):
        print(f"node {v} = {in_time[v]}/{out_time[v]}")


if __name__ == "__main__":
    main()