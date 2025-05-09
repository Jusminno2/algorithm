N = int(input())
count = 0

for i in range(1, N+1, 2):
    yakusu = 0

    for j in range(1, N+1):
        if i % j == 0:
            yakusu += 1
    if yakusu == 8:
        count += 1

print(count)

