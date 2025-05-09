N = int(input())
count = 0

for i in range(1, N+1):

    if 1 <= (i//10**4) < 10:
        count += 1
    elif 1 <= (i//10**2) < 10:
        count += 1
    elif 1 <= i <= 9:
        count += 1

print(count)
