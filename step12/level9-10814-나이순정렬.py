# https://www.acmicpc.net/problem/10814

import sys

N = int(sys.stdin.readline())

array = []

for i in range(N):
    [a, b] = sys.stdin.readline().split()
    a = int(a)
    array.append([a,b])

array.sort(key=lambda x : x[0])

for i in range(N):
    print(array[i][0], array[i][1])
