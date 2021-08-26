# https://www.acmicpc.net/problem/1181

import sys

N = int(sys.stdin.readline())

array = []

for i in range(N):
    a = sys.stdin.readline().strip()
    if a not in array:
        array.append(a)

array.sort(key=lambda x : (len(x), x))

for i in range(len(array)):
    print(array[i])
