def solve():
    N = int(input())
    A = list(map(int, input().split()))

    used = [0] * N
    ans = 1
    last = 0

    while True:
        if A[last] * 2 >= A[N-1]:
            ans += 1
            break

        nxt = -1
        for i in range(1, N):
            if used[i]:
                continue
            if A[last] * 2 >= A[i]:
                if nxt != -1 and A[nxt] >= A[i]:
                    continue
                nxt = i

        if nxt == -1 or A[nxt] >= A[last]:
            print(-1)
            return

        ans += 1
        last = nxt
        used[nxt] = 1

    print(ans)


def main():
    T = int(input())
    for _ in range(T):
        solve()


if __name__ == '__main__':
    main()