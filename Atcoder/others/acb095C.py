A, B, C, X, Y = map(int, input().split())

total = 0
total_list = []

if X >= Y:
    ab_pizza_max = 2*X
else:
    ab_pizza_max = 2*Y

for i in range(0, ab_pizza_max+1, 2):
    if i == 0:
        total = A*X + B*Y
        total_list.append(total)
    elif i % 2 == 0:
        a_num = X - i//2
        b_num = Y - i//2

        if a_num < 0:
            a_num = 0
        if b_num // 2 < 0:
            b_num = 0
        total = A * a_num + B * b_num + C * i
        total_list.append(total)

print(min(total_list))