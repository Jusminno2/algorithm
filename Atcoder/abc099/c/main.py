INF = 10**7
memo = {}

def f(cu):
    if cu == 0:
        return 0
    if cu in memo:
        return memo[cu]

    res = INF

    # 1 yen
    res = min(res, f(cu - 1) + 1)

    # 6 yen
    x = 6
    while x <= cu:
        res = min(res, f(cu - x) + 1)
        x *= 6

    # 9 yen coins
    x = 9
    while x <= cu:
        res = min(res, f(cu - x) + 1)
        x *= 9

    memo[cu] = res
    return res


def main():
    N = int(input())
    print(f(N))


if __name__ == '__main__':
    main()

