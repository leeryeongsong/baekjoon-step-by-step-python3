# https://www.acmicpc.net/problem/11650

import sys

N = int(sys.stdin.readline())

array = []

for i in range(N):
    [a, b] = map(int, sys.stdin.readline().split())
    array.append([a,b])

array.sort()

for i in range(N):
    print(array[i][0], array[i][1])
