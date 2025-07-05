import bisect
from itertools import accumulate

Q = int(input())
c = list()
x = list()

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        c.append(query[1])
        x.append(query[2])
        # insertion_list = [x] * c
        # A = A + insertion_list
        # print(A)
        # print("c after q1: ", c)
        # print("x after q1: ", x)

    elif query[0] == 2:
        k = int(query[1])
        S = list(accumulate(c))
        ans = 0
        insert_id = bisect.bisect_left(S, k)
        # print("S:", S)
        # rest = k - S[insert_id-1]
        rest = S[insert_id] - k
        if insert_id == 0:
            k_rest = k
        else:
            k_rest = k - S[insert_id-1]
        # print(k_rest)
        # print("rest after insertion: ", rest)
        # 及ばなかったところを消す
        # c[insert_id] = c[insert_id] - rest
        c[insert_id] = rest
        # print("c before q2: ", c)
        # 解答
        if insert_id == 0:
            # print("Yes")
            print(k*x[0])
        else:
            for i in range(insert_id):
                # print("c[i] after q2: ", c[i])
                # print("x[i] after q2: ", x[i])
                ans = c[i] * x[i]
            # print("ans: ", ans)
            # print("k_rest: ", k_rest)
            # print("c: ", c)
            # print("insert: ", insert_id)
            ans += k_rest * x[insert_id]
            print(ans)
        # その前ふつうに削除
        del c[:insert_id]
        del x[:insert_id]
        # print("c after q2: ", c)
        # delete_list = A[:k]
        # del A[:k]
        # print(sum(delete_list))

