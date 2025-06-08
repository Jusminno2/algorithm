n = int(input())
T = input()
A = input()

for i in range(n):
    if T[i] == A[i] and T[i] == "o":
        print("Yes")
        exit()

print("No")