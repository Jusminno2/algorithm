import collections

S = input()

c = collections.Counter(S)
max_key = max(c, key=c.get)

first = None
second = None

check = list()
for i in range(len(S)):
    if S[i] == max_key:
        check.append(i)
if check:
    if len(check) >= 2:
        first = check[0]
        second = check[-1]
    else:
        print(0)
        exit()
else:
    print(0)
    exit()

if first == second or (second-first+1) < 3:
    print(0)
    exit()

count = 0
for t in range(first, second+1):
    if S[t] == max_key:
        count += 1

print((count-2) / (second-first-1))


