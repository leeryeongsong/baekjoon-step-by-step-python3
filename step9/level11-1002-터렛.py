# https://www.acmicpc.net/problem/1002

# 메모리 31312KB 시간 76ms
import sys
import math

T = int(sys.stdin.readline())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        xy = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        rr = r1 + r2 
        if xy == rr or xy == (r2 - r1) or xy == (r1 - r2):
            print(1)       
        elif xy < (r2 - r1) or xy < (r1 - r2):
            print(0)
        elif xy > rr:
            print(0)
        else:
            print(2)
