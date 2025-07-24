N = int(input())

for i in range(101):
    for j in range(101):
        if 4*i + 7*j == N:
            print('Yes')

print('No')