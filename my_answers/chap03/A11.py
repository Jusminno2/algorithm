from typing import List


def binary_search(x: int, A: List[int], N: int) -> int:
    L = 0
    R = N-1
    while L <= R:
        mid = (L + R) // 2
        if x < A[mid]:
            R = mid - 1
        if x == A[mid]:
            return mid
        if x > A[mid]:
            L = mid + 1
    return -1


if __name__ == '__main__':
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    print(binary_search(X, A)+1)
