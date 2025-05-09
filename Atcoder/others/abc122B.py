S = input()
target = ["A", "T", "G", "C"]
current_length = 0
max_len = 0

for s in S:
    if s in target:
        current_length += 1
        max_len = max(max_len, current_length)
    else:
        current_length = 0

print(max_len)

