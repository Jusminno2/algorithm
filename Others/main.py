while True:

    H, W = map(int, input().split())

    MIN_H = 3
    MAX_H = 300

    MIN_W = 3
    MAX_W = 300

    if H == 0 and W == 0:
        break

    if MIN_H > H or H > MAX_H:
        break

    if MIN_W > W or W > MAX_W:
        break

    for i in range(H):
        for j in range(W):
            if i == 0 or i == H - 1:
                print("#", end="")
            elif j == 0 or j == W - 1:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()

