S = input()
new_s = ""

for s in S:
    if s == "1":
        new_s = new_s + "0"
    elif s == "0":
        new_s = new_s + "1"

print(new_s)
