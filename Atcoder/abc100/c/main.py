N = int(input())
A = list(map(int, input().split()))

ans = 0

"""
example:
3
5 2 4
"""

for i in range(N):
    count = 0
    if A[i] % 2 == 0:
        while A[i] % 2 == 0:
            A[i] //= 2
            count += 1
        ans += count

print(ans)

