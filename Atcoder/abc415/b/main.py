S = input()
count = 0
array = list()

for i, s in enumerate(S):

    if s == '.':
        continue
    elif s == '#':
        array.append(i+1)
        count += 1
        if count >= 2:
            a, b = array[0], array[-1]
            print(f"{a},{b}")
            count = 0
            array = list()

