S = input()
upper = list()

for s in S:
    if s.isupper():
        upper.append(s)

print("".join(upper))

