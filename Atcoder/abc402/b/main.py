from collections import deque

q = int(input())
array = deque()
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        array.append(query[1])
    else:
        order = array.popleft()
        print(order)
