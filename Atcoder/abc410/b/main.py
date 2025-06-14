from operator import index

N, Q = map(int, input().split())
X = list(map(int, input().split()))

arr = [0 for i in range(N)]
ans = []

for x in X:
    if x > 0:
        arr[x - 1] += 1
        ans.append(x)
    elif x == 0:
        min_id = arr.index(min(arr))
        arr[min_id] += 1
        ans.append(min_id+1)


print(" ".join(map(str, ans)))

