def dfs(G, seen, n, pre_order, last_order,  time):

    time[0] += 1
    seen[n] = True
    pre_order[n].append(time[0])

    for next_n in G[n]:
        if seen[next_n]:
            continue
        else:
            dfs(G, seen, next_n, pre_order, last_order, time)

    time[0] += 1
    last_order[n].append(time[0])


if __name__ == '__main__':
    n = int(input())
    seen = [False] * (n + 1)
    G = [[] for _ in range(n + 1)]
    pre_order = [[] for _ in range(n + 1)]
    last_order = [[] for _ in range(n + 1)]
    time = [0]

    for _ in range(n):
        arr = list(map(int, input().split()))
        if arr[1] == 0:
            continue
        else:
            for i in range(arr[1]):
                G[arr[0]].append(arr[i + 2])

    # print(G)
    dfs(G, seen, 1, pre_order, last_order, time)
    # print(time)
    # print(pre_order)
    # print(last_order)

    for i in range(1, n+1):
        print(f"{i} {pre_order[i][0]} {last_order[i][0]}")