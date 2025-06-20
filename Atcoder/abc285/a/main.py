a, b = map(int, input().split())
G = [[1,2], [3,4], [5,6], [7,8], [9,10], [11, 12], [13,14], [4], [4], [5], [5], [6], [6], [7], [7]]

a = a-1
b = b-1

if b in G[a]:
    print("Yes")
else:
    print("No")