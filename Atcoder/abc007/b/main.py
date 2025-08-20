import string

A = input()
if A == 'a':
    print(-1)
else:
    for a in A:
        for i in string.ascii_letters:
            if a > i:
                print(i)
                exit()
