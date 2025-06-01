n, s = map(int, input().split())
T = list(map(int, input().split()))

for idx, t in enumerate(T):
    if idx == 0:
        if t < s+0.5:
            continue
        else:
            print("No")
            exit()
    else:
        if T[idx]-T[idx-1] < s+0.5:
            continue
        else:
            print("No")
            exit()


print("Yes")
