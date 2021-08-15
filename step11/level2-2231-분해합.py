# https://www.acmicpc.net/problem/2231

import sys

N = int(sys.stdin.readline())
saengseong = []

for i in range(N):
    if i + sum([int(j) for j in str(i)]) == N:
        saengseong.append(i)

if len(saengseong) >= 1:
    print(min(saengseong))
else:
    print(0)
