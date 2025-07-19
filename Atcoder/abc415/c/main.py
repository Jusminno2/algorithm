import itertools

T = int(input())

for _ in range(T):
    N = int(input())
    S = input()

    bit = "0" * N
    list_N = [str(i) for i in range(1, N+1)]

    for i in range(N):
        c_list = list(itertools.combinations(list_N, i))
        print(i, c_list)
        for c in c_list:
            pass















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


