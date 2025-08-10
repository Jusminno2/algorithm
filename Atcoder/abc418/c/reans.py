def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    max_val = max(a)

    # 累積和とカウントの配列を初期化
    # sum[y]: A_i ≤ y である i に対する A_i の総和
    # cnt[y]: A_i ≤ y を満たす i の個数
    sum_arr = [0] * (max_val + 1)
    cnt_arr = [0] * (max_val + 1)

    # i=1,...,N について、cnt[A_i] に 1 を、sum[A_i] に A_i を加える
    for val in a:
        cnt_arr[val] += 1
        sum_arr[val] += val
    # print(f'最初の sum_arr: {sum_arr}')
    # print(f'最初の cnt_arr: {cnt_arr}')

    for y in range(1, max_val + 1):
        cnt_arr[y] += cnt_arr[y - 1]  # cnt[y] = cnt[y-1] + cnt[y]
        sum_arr[y] += sum_arr[y - 1]  # sum[y] = sum[y-1] + sum[y]
    # print(f'累積和後の sum_arr: {sum_arr}')
    # print(f'累積和後の cnt_arr: {cnt_arr}')

    # query start
    for _ in range(q):
        b = int(input())

        # 範囲内かどうかチェック
        if b-1 < 0:
            sum_below = 0
            count_below = 0
        elif b-1 > max_val:
            # すべての要素が b-1 以下の場合
            sum_below = sum_arr[max_val]
            count_below = cnt_arr[max_val]
        else:
            # b-1 よりも大きい要素が含まれる場合
            sum_below = sum_arr[b-1]
            count_below = cnt_arr[b-1]

        if count_below == n:
            print(-1)

        else:
            count_above = n - count_below
            ans = 1 + sum_below + count_above * (b-1)
            # print(ans)


if __name__ == '__main__':
    main()

