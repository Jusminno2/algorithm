def solve():
    s = input().strip()
    n = len(s)
    ans = 0

    # 最初のtを見つけるまで探索する！
    for i in range(n):
        if s[i] != 't':
            continue
        # 次のtを見つけるまで探索する！
        for j in range(i + 2, n):
            if s[j] != 't':
                continue

            # xはカウンターを表す！
            x = 0
            # iを固定、jを変数として（i,j）の幅を探索する
            for ki in range(i, j+1):
                if s[ki] == 't':
                    x += 1

            # 1つの幅で探索が終わったら、一旦充填率を計算 => 結果的に最大値を求める
            length = j - i + 1
            item = (x-2) / (length-2)

            if item > ans:
                ans = item

    print(ans)


if __name__ == '__main__':
    solve()