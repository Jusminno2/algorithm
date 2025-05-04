N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

Alice = []
Bob = []

i = 0
# for ループで隅奇を場合分けするもよし
while i <= N-1:
    if i == N-1:
        Alice.append(a[i])
        break

    Alice.append(a[i])
    Bob.append(a[i+1])
    i += 2

diff = sum(Alice) - sum(Bob)

print(diff)


