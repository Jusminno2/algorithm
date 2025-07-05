import bisect
from itertools import accumulate

Q = int(input())
c = list()
x = list()

"""
愚直にappendしていってsumで線形探索すると計算量O(Q✕c)となりだめ
-> データの持ち方を工夫して、cとxを別々で持った
-> 累積和を別で用意しており、二分探索でkが入るindexを調査
-> index == 0 のときは別途対応した
-> それまでのデータを削除（x,cともに）
"""


for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        c.append(query[1])
        x.append(query[2])

    elif query[0] == 2:
        k = int(query[1])
        S = list(accumulate(c))
        ans = 0
        insert_id = bisect.bisect_left(S, k)
        rest = S[insert_id] - k
        if insert_id == 0:
            k_rest = k
        else:
            k_rest = k - S[insert_id-1]
        c[insert_id] = rest
        if insert_id == 0:
            # print("Yes")
            print(k*x[0])
        else:
            for i in range(insert_id):
                ans = c[i] * x[i]
            ans += k_rest * x[insert_id]
            print(ans)
        del c[:insert_id]
        del x[:insert_id]

