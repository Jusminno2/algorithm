S = input()

length = len(S) - 1
ans = list()
sum = 0

for i in range(1 << length):
    id_list = list()
    S_list = [s for s in S]
    gap = 0
    for j in range(length):
        if i & (1 << j):
            id_list.append(j)

    for id in id_list:
        S_list.insert(id+gap+1, "+")
        gap += 1

    if not '+' in S_list:
        sum += int(''.join(S_list))
    else:
        culc = ''.join(S_list)
        culc_list = culc.split('+')
        for i in culc_list:
            sum += int(i)

print(sum)






