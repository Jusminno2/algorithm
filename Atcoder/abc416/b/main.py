S = input()
S_arr = [s for s in S]

for i in range(len(S)):
    for j in range(len(S)):
        if S_arr[i] == '#':
            continue
        else:
            if S_arr[i] == S_arr[j]:
                slice = S_arr[i+1:j]
                if '#' in slice:
                    S_arr[i] = 'o'
                    S_arr[j] = 'o'
                else:
                    S_arr[i] = '.'

print(''.join(S_arr))
