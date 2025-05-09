S = input()
alpha = [chr(97+i) for i in range(26)]

for i in alpha:
    if not i in S:
        print(i)
        break