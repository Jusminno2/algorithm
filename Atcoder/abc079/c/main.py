input_num = input()
n = 3

for i in range(2 ** n):
    op = []
    total = int(input_num[0])
    for j in range(n):
        if ((i >> j) & 1):
            op.append('+')
            total += int(input_num[j+1])
        else:
            op.append('-')
            total -= int(input_num[j+1])
    if total == 7:
        print(f"{input_num[0]}{op[0]}{input_num[1]}{op[1]}{input_num[2]}{op[2]}{input_num[3]}=7")
        exit()
