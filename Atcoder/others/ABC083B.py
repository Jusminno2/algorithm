N, A, B = map(int, input().split())
total = 0

for i in range(1, N+1):
    a = i // 10000
    b = (i - a*10000) // 1000
    c = (i - a*10000 - b*1000) // 100
    d = (i - a*10000 - b*1000 - c*100) // 10
    e = i - a*10000 - b*1000 - c*100 - d*10
    sum_num = a + b + c + d + e

    if A <= sum_num <= B:
        total += i

print(total)

