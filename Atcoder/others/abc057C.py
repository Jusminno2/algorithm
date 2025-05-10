N = int(input())
N_digits = list()

def culc(A, B):
    a_keta = 1
    b_keta = 1

    for i in range(1, 11):
        if A // (10**i) >= 1:
            a_keta += 1
        if B // (10**i) >= 1:
            b_keta += 1

    if a_keta >= b_keta:
        return a_keta
    else:
        return b_keta


# √N までしか考えなくて良い
for i in range(1, int(N**0.5)+1):
    if N % i == 0:
        if i not in N_digits:
            N_digits.append(i)
            N_digits.append(N//i)
        else:
            break


result = list()
for i in range(0, len(N_digits), 2):
    result.append(culc(N_digits[i], N_digits[i+1]))


print(min(result))
