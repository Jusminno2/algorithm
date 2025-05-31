n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

count = 0

def binary_search(array, item):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == item:
            return True
        elif array[mid] > item:
            right = mid - 1
        else:
            left = mid + 1

for t in T:
    if binary_search(S, t):
        count += 1


print(count)