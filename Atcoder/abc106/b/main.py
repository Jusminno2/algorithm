N = int(input())

ans = list()

for i in range(1, N+1):
    divisors = list()
    if i % 2 != 0:
        for j in range(1, i+1):
            if i % j == 0:
                divisors.append(j)
        if len(divisors) == 8:
            ans.append(i)

print(len(ans))

