#!/usr/bin/env python
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
A = list(map(int, input().split()))
sum_num = 0

for i in range(N):
    if i % 2 == 0:
        sum_num += A[i]


print(sum_num)

