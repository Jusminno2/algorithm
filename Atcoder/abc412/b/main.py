S = input()
T = input()

for i in range(len(S)):
    if i > 0:
        if S[i].isupper():
            if S[i - 1] not in T:
                print("No")
                exit()

print("Yes")

