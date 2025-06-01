from collections import deque
from typing import List


def bfs(G: List[int], n: int) -> List[int]:
    q = deque()
    dist = [0] * (n+1)
    visited = [False] * (n+1)
    q.append(1)
    visited[1] = True
    dist[1] = 0
    
    while q:
        v = q.popleft()
        for next_v in G[v]:
            if next_v not in q:
                visited[next_v] = True
                dist[next_v] = dist[v] + 1  # めっちゃポイント！！！！
                q.append(next_v)
    return dist


def main():
    n = int(input())
    G = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        arr = list(map(int, input().split()))
        u = arr[0]
        k = arr[1]
        if k != 0:
            # G[i] = arr[2:]
            G[u] = arr[2:]


    dist = bfs(G, n)
    for i in range(1, n + 1):
        print(f"{str(i)} {str(dist[i])}")


if __name__ == '__main__':
    main()

