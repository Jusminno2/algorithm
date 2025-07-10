def main():
    N = int(input())
    A = list(map(int, input().split()))

    A = [0] + A  # 1-index に揃える

    dp = [[0] * 21 for _ in range(N + 1)]

    # 最初の値を初期化（A[1] が 0〜20 の範囲外なら無視）
    if 0 <= A[1] <= 20:
        dp[1][A[1]] = 1

    for i in range(2, N):
        a = A[i]
        for v in range(21):
            cnt = dp[i - 1][v]
            if cnt == 0:
                continue
            if 0 <= v + a <= 20:
                dp[i][v + a] += cnt
            if 0 <= v - a <= 20:
                dp[i][v - a] += cnt

    # 最後のターゲット値 A[N] が 0〜20 の範囲にあるかチェック
    ans = dp[N - 1][A[N]] if 0 <= A[N] <= 20 else 0
    print(ans)


if __name__ == "__main__":
    main()
