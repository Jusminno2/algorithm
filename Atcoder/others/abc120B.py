A, B, K = map(int, input().split())
common_list = list()

if A>=B:
    for i in range(1, B+1):
        if A % i == 0 and B % i == 0:
            common_list.append(i)

elif A<B:
    for i in range(1, A+1):
        if A % i == 0 and B % i == 0:
            common_list.append(i)

common_list.reverse()

print(common_list[K-1])