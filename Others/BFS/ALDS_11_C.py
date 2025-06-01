from collections import deque
from typing import List

def bfs(G: List[int], n: int) -> List[int]:
    queue = deque()
    queue.append(1)
    dist = [-1] * (n + 1)
    dist[1] = 0  # スタート地点は距離0

    while queue:
        v = queue.popleft()
        for next_v in G[v]:
            if dist[next_v] == -1:  # まだ到達していないノード
                dist[next_v] = dist[v] + 1
                queue.append(next_v)

    return dist

def main():
    n = int(input())
    G = [[] for _ in range(n+1)]
    for _ in range(n):
        arr = list(map(int, input().split()))
        u = arr[0]
        k = arr[1]
        G[u] = arr[2:]

    dist = bfs(G, n)

    for i in range(1, n+1):
        print(f"{i}: {dist[i]}")

if __name__ == "__main__":
    main()
