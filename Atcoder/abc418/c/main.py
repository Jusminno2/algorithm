import bisect
import itertools

N, Q = map(int, input().split())
A = list(map(int, input().split()))
max_A = max(A)
sum_A = sum(A)
A.sort()
acc_A = list(itertools.accumulate(A))
print(A)
print(acc_A)

for _ in range(Q):
    b = int(input())
    if b > max_A:
        print(-1)
    else:
        insert_idx = bisect.bisect_left(A, b)
        if insert_idx == 0:
            print(b)
        elif insert_idx == len(A)-1:
            print(acc_A[insert_idx])
        else:
            print(N * acc_A[insert_idx-1] + 1)



