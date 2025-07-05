N = int(input())
array = [input() for _ in range(N)]

list = []

for i in range(N):
    for j in range(i + 1, N):
        s1 = array[i] + array[j]
        s2 = array[j] + array[i]
        if s1 not in list:
            list.append(s1)
        if s2 not in list:
            list.append(s2)

print(len(list))
