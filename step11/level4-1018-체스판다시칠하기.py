# https://www.acmicpc.net/problem/1018

import sys

M, N = map(int, sys.stdin.readline().split())

screen = [[0]*N for i in range(M)]

for i in range(M):
    screen[i] = list(sys.stdin.readline().strip())

Wfirst = []
Bfirst = []

for i in range(M-7):
    for j in range(N-7):
        Wcount = 0
        Bcount = 0
        for k in range(8):
            for l in range(8):
                if k%2==0 and l%2==0:
                    if screen[i+k][j+l] == 'W':
                        Bcount += 1
                    else:
                        Wcount += 1
                if k%2==0 and l%2!=0:
                    if screen[i+k][j+l] == 'W':
                        Wcount += 1
                    else:
                        Bcount += 1

                if k%2!=0 and l%2==0:
                    if screen[i+k][j+l] == 'W':
                        Wcount += 1
                    else:
                        Bcount += 1

                if k%2!=0 and l%2!=0:
                    if screen[i+k][j+l] == 'W':
                        Bcount += 1
                    else:
                        Wcount += 1
        Wfirst.append(Wcount)
        Bfirst.append(Bcount)

Wmin = min(Wfirst)
Bmin = min(Bfirst)
mini = min(Wmin, Bmin)
print(mini)
