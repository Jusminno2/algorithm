N = int(input())

l = [0] * 87
l[0] = 2
l[1] = 1

for i in range(1, N):
    l[i+1] = l[i] + l[i - 1]

print(l[N])