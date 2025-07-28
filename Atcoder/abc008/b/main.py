from collections import defaultdict

N = int(input())
d = defaultdict(int)
for _ in range(N):
    k = input()
    d[k] += 1
score_sorted = sorted(d.items(), key=lambda x:x[1], reverse=True)

d = dict(score_sorted)

for k, v in d.items():
    print(k)
    exit()

