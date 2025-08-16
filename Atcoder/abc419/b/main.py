from collections import deque

Q = int(input())
arr = list()

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        arr.append(query[1])
        arr.sort()
    elif query[0] == 2:
        ans = arr.pop(0)
        print(ans)

