import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

num = list(i for i in range(1, N+1))

ptn = list(itertools.permutations(num))
a = 0
b = 0

for id, p in enumerate(ptn):
    if list(p) == P:
        a = id + 1
    if list(p) == Q:
        b = id + 1

print(abs(a - b))
