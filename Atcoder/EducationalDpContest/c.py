def main():
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]

    # dpテーブルの初期化=>この3次元化が肝になる
    dp = [[0] * 3 for _ in range(N+1)]

    # dp遷移
    for i in range(N):  # i日目
        for j in range(3):  # 今日の活動
            for k in range(3):  # 明日の活動
                if j == k:
                    continue
                dp[i+1][k] = max(dp[i+1][k], dp[i][j] + a[i][k])    # a[i][k] はポイント

    print(max(dp[N]))


if __name__ == '__main__':
    main()