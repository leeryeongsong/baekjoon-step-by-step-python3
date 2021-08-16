# https://www.acmicpc.net/problem/7568

import sys

N = int(sys.stdin.readline())
x = [0 for i in range(N)]
y = [0 for i in range(N)]
rank = [1 for i in range(N)]

for i in range(N):
    x[i], y[i] = map(int, sys.stdin.readline().split())

for i in range(N):
    for j in range(N):
        if i !=j and x[i] < x[j] and y[i] < y[j]:
            rank[i] += 1

for i in range(N):
    print(rank[i], end=' ')
