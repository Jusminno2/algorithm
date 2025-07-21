S = input()
S_list = [s for s in S]

length = len(S) - 1
ans = list()

for i in range(1 << length):
    id_list = list()
    gap = 0
    for j in range(length):
        if i & (1 << j):
            id_list.append(j)
    for id in id_list:
        S_list.insert(id+gap+1, "+")
        gap += 1
    print(S_list)

    "+でsplitしたらええか"




