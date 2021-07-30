# https://www.acmicpc.net/problem/5622

"""
# 메모리 29200KB 시간 72ms 코드 길이 373B
words = input()
sec = 0

for i in words:
    if i in 'ABC':
        sec += 3
    elif i in 'DEF':
        sec += 4
    elif i in 'GHI':
        sec += 5
    elif i in 'JKL':
        sec += 6
    elif i in 'MNO':
        sec += 7
    elif i in 'PQRS':
        sec += 8
    elif i in 'TUV':
        sec += 9        
    elif i in 'WXYZ':
        sec += 10

print(sec)
"""

# 메모리 29200KB 시간 72ms 코드 길이 194B
words = input()
sec = 0
ABC = ['ABC', 'DEF', 'GHI', 'JKL','MNO', 'PQRS', 'TUV', 'WXYZ']

for i in words:
    for j in range(8):
        if i in ABC[j]:
            sec += 3+j
        
print(sec)
