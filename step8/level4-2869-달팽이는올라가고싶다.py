# https://www.acmicpc.net/problem/2869

"""
# 값이 커지면 시간 오래 걸림
A, B, V =map(int, input().split())
R = 0
day = 0

while R < V:
    day += 1
    R += A
    if R >= V:
        break
    R -= B

print(day)

"""

# 메모리 31312KB, 시간 84ms, 코드 길이 80B
import math

A, B, V =map(int, input().split())

print(math.ceil((V-A)/(A-B))+1)
