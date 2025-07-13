N = int(input())
s = ""
length = 0

for _ in range(N):
    c, l = input().split()
    l = int(l)

    if l > 100:
        print("Too Long")
        exit()
    else:
        for _ in range(l):
            s += c
        length += l



if length > 100:
    print("Too Long")
else:
    print("".join(s))

