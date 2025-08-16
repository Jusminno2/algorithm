N, M = map(int, input().split())
S = list(input())
T = list(input())


for _ in range(M):
    L, R = map(int, input().split())
    L = L - 1
    R = R - 1
    S_left = S[:L]
    S_mid = S[L:(R+1)]
    S_right = S[(R+1):]
    T_left = T[:L]
    T_mid = T[L:(R+1)]
    T_right = T[(R+1):]
    S = S_left + T_mid + S_right
    T = T_left + S_mid + T_right

print(''.join(map(str, S)))



