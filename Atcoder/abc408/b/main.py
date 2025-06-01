n = int(input())
A = list(map(int, input().split()))

A = set(A)
C = list(A)
C.sort()

print(len(C))
print(" ".join(map(str, C)))