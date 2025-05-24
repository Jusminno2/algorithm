num = input()

if num[0] == num[1] and num[1] == num[2]:
    print("Yes")
elif num[1] == num[2] and num[2] == num[3]:
    print("Yes")
else:
    print("No")
