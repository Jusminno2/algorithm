import itertools

T = int(input())

for _ in range(T):
    N = int(input())
    S = input()

    list_N = [str(i) for i in range(1, N+1)]

    for i in range(1, N+1):
        c_list = list(itertools.combinations(list_N, i))
        count = 0
        for c in c_list:
            status = 0
            c_int = list(map(int, c))
            for j in range(len(c_int)):
                status += 2 ** (c_int[j]-1)
            if S[status] == "1":
                count += 1
        if count == len(c_list):
            print("No")
            break

        print("Yes")




















    # ones = '1' * (2**N - 1)
    # # ones を10進数変換
    # ones_10 = int(ones, 2)
    # # S を10進数変換
    # S_10 = int(S, 2)
    #
    # if ones_10 & S_10:
    #     print(ones)
    #     print("Yes")
    #     print("one point: ", ones_10 & S_10)
    #     print("bit: ", bin(ones_10 & S_10))


