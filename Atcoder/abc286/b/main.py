N = int(input())
S = input()
ans = ""

for i in range(N):
    if i == N-1:
        ans += S[i]
    elif S[i] == "n" and S[i+1] == "a":
        ans += S[i]
        ans += "y"
    else:
        ans += S[i]

print(ans)

