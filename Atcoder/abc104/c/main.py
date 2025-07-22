D, G = map(int, input().split())
points = [100 * int(i+1) for i in range(D)]
scores = list()
for i in range(D):
    scores.append(list(map(int, input().split())))

tmp = 0
count = 0
