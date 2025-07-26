N, L, R = map(int, input().split())
S = input()
ans = 0

for i, s in enumerate(S):
    if L-1 <= i <= R-1:
        if s == 'o':
            ans += 1
        else:
            print('No')
            exit()
if ans == R-L+1:
    print('Yes')
else:
    print('No')