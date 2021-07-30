# https://www.acmicpc.net/problem/2908

"""
# 메모리 29200KB 시간 72ms 
def rev(x):
    rev_x = x[::-1]
    return int(rev_x)

A, B = input().split()
print(max(rev(A), rev(B)))
"""

"""
# 메모리 29200KB 시간 72ms 
def rev(x):
    rev_x = ''.join(reversed(x))
    return int(rev_x)

A, B = input().split()
print(max(rev(A), rev(B)))
"""

# 메모리 29200KB 시간 72ms 
def rev(x):
    rev_x = ''
    for i in x:
        rev_x = i + rev_x
    return int(rev_x)

A, B = input().split()
print(max(rev(A), rev(B)))
