from collections import Counter

N = int(input())
A = list(map(int, input().split()))

count = 0

'''
j - i = A[i] + A[j] を式変形するという考えまでは良かった
=> j - A[j] = i + A[i] としたときに、i + A[i] で表すことのできる数を数え上げる（Counter）
=> その後、j - A[j] について数え上げていき、何個一致するものがあるのかを考える
'''

Ai_plus_i = list()
for i in range(N):
    Ai_plus_i.append(A[i] + i)

# 和で表せる数とその登場回数をCounterオブジェクトで作成
Ai_plus_i = Counter(Ai_plus_i)

# print(Ai_plus_i)

# j - A[j] で表現できる数は何個あるのか？
for j in range(N):
    # print(j-A[j])
    if Ai_plus_i[j - A[j]]:
        count += Ai_plus_i[j - A[j]]

print(count)
