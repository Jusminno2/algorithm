def binary_search(arr, item):
    left, right = 0, len(arr) - 1
    while abs(right - left) > 1:
        mid = (left + right) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            right = mid
        else:
            left = mid
    if item < (arr[left]+arr[right]) // 2:
        return left
    else:
        return right


def main():
    d = int(input())
    n = int(input())
    m = int(input())

    d_arr = [0]
    for _ in range(n - 1):
        d_arr.append(int(input()))
    d_arr.append(d)

    d_sorted = sorted(d_arr)

    length = 0

    for _ in range(m):
        k = int(input())
        length += abs(k - d_sorted[binary_search(d_sorted, k)])
    print(length)


if __name__ == '__main__':
    main()