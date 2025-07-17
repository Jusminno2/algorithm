n = int(input())
a = [0 for _ in range(n + 1)]

for i in range(1, n+1):

    if i == 1 or i == 2:
        a[i] = 0

    elif i == 3:
        a[i] = 1

    else:
        a[i] = a[i - 1] + a[i - 2] + a[i - 3]

print(a[n] % 10007)