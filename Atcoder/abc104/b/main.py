S = input()
count = 0

for i, s in enumerate(S):
    if i == 0 and s == "A":
        if 2 <= i <= len(S) and s == "C":
            count += 1

    else:
        print("WA")
        exit()

if count == 1:
    print("AC")
else:
    print("WA")


