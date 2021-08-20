# https://www.acmicpc.net/problem/2751

import sys

N = int(sys.stdin.readline())
Num = []

for i in range(N):
    a = int(sys.stdin.readline())
    Num.append(a)

Num.sort()

for i in range(N):
    print(Num[i])
