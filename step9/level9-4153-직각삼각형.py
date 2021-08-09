# https://www.acmicpc.net/problem/4153

import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0:
        break
    if a == max(a, b, c):
        if a*a == b*b + c*c:
            print('right')
            continue
        
    elif b == max(a, b, c):
        if  b*b == a*a + c*c:
            print('right')
            continue
    elif c == max(a, b, c):
        if  c*c == a*a + b*b:
            print('right')
            continue    
    print('wrong')    
