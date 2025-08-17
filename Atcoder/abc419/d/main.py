N, M = map(int, input().split())
s = input()
t = input()

cum = [0] * (N+1)

# いもす法 - Point 1 => 範囲のスタート+1, 範囲の末尾の次を-1
for _ in range(M):
    l, r = map(int, input().split())
    cum[l-1] += 1
    cum[r] -= 1

# いもす法 - Point 2 => 前からじゃんじゃん足していく
for i in range(N):
    cum[i + 1] =+ cum[i]

# もし偶数回スワップ => 元の位置｜奇数回スワップ => t の文字列
ans = [s[i] if cum[i] % 2 == 0 else t[i] for i in range(N)]
print(''.join(ans))