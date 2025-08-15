def check(x):
    time = list()
    for i in range(N):
        time.append((x-H[i]) // S[i])
    time.sort()
    for n in range(N):
        if time[n] < n:
            return False
    return True


def meguru_bisect(left, right):
    while (abs(right - left) > 1):
        mid = (right + left) // 2
        if check(mid):
            right = mid
        else:
            left = mid
    return right


if __name__ == '__main__':
    N = int(input())
    H = [0] * N
    S = [0] * N
    for i in range(N):
        H[i], S[i] = map(int, input().split())
    print(meguru_bisect(0, int(1e+14)))