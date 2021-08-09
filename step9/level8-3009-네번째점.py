# https://www.acmicpc.net/problem/3009

import sys

x = [0, 0, 0]
y = [0, 0, 0]
for i in range(3):
    x[i], y[i] = map(int, sys.stdin.readline().split())

for j in x:
    if x.count(j) == 1:
        a = j
for k in y:
    if y.count(k) == 1:
        b = k

print(a, b)
