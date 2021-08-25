# https://www.acmicpc.net/problem/11651

"""
# 틀렸습니다.
import sys

N = int(sys.stdin.readline())

array = []

for i in range(N):
    [a, b] = map(int, sys.stdin.readline().split())
    array.append([a,b])

array.sort(key=lambda x : x[1])

for i in range(N):
    print(array[i][0], array[i][1])
"""


# 성공
import sys

N = int(sys.stdin.readline())

array = []

for i in range(N):
    [a, b] = map(int, sys.stdin.readline().split())
    array.append([a,b])

array.sort(key=lambda x : (x[1], x[0]))

for i in range(N):
    print(array[i][0], array[i][1])
