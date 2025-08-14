import math

N = int(input())

for i in reversed(range(100000)):
    if i ** 2 <= N:
        print(i ** 2)
        exit()

