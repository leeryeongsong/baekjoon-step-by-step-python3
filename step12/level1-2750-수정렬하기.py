# https://www.acmicpc.net/problem/2750

# 삽입 정렬
import sys

N = int(sys.stdin.readline())
Num = []

for i in range(N):
    a = int(sys.stdin.readline())
    Num.append(a)
    if i > 0:
        for j in range(i):
            if Num[i-j] < Num[i-j-1]:
                b = Num[i-j]
                Num[i-j] = Num[i-j-1]
                Num[i-j-1] = b

for i in range(N):
    print(Num[i])
