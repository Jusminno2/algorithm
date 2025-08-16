n = int(input())
r = list(0 for _ in range(n))
c = list(0 for _ in range(n))

# 配列用意
for i in range(n):
    r[i], c[i] = list(map(int, input().split()))

# # 動き
# dx = [1, 0, -1, 0, 1, 1, -1, -1]
# dy = [0, 1, 0, -1, 1, -1, 1, -1]
#
# # 時間チェック
# def culc_time(x):
#     time = list()
#     for i in range(n):
#         time.append(min())
#
#6

# # 二分探索
# def meguru_bisect(left, right):
#     while abs(right - left) > 1:
#         mid = (left + right) // 2
#         if culc_time(mid) < left:
#             right = mid
#         else:
#             left = mid
#     return right

r.sort()
c.sort()

r_diff = r[-1] - r[0]
c_diff = c[-1] - c[0]

if r_diff > c_diff:
    # print(r_diff / 2)
    print((r_diff+2-1) // 2)
else:
    # print(c_diff / 2)
    print((c_diff + 2 - 1) // 2)