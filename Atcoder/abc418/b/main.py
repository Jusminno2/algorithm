S = input()

first = None
second = None

check = list()
for i in range(len(S)):
    if S[i] == 't':
        check.append(i)
if check and len(check) >= 2:
    first = check[0]
    second = check[-1]
else:
    print(0)
    exit()

if first == second or (second-first+1) < 3:
    print(0)
    exit()

count = 0
for t in range(first, second+1):
    if S[t] == 't':
        count += 1

print((count-2) / (second-first-1))
