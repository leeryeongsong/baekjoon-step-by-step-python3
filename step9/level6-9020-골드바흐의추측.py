# https://www.acmicpc.net/problem/9020

"""
# 시간 초과
import math

def is_prime_number(n):
    array = [True for i in range(n+1)] 
    for i in range(2, int(math.sqrt(n)) + 1): 
        if array[i] == True: 
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    return [ i for i in range(2, n+1) if array[i] ]

T = int(input())

for i in range(T):
    n = int(input())
    prime_num = is_prime_number(n)
    for j in range(-1, -len(prime_num)-1,-1):
        if prime_num[j] <= n//2:
            if n-prime_num[j] in prime_num:
                print(prime_num[j], n-prime_num[j])
                break
"""

"""
# 시간 초과
import math
import sys

def is_prime_number(n):
    array = [True for i in range(n+1)] 
    for i in range(2, int(math.sqrt(n)) + 1): 
        if array[i] == True: 
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    return [ i for i in range(2, n+1) if array[i] ]

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    prime_num = is_prime_number(n)
    for j in range(-1, -len(prime_num)-1,-1):
        if prime_num[j] <= n//2:
            if n-prime_num[j] in prime_num:
                print(prime_num[j], n-prime_num[j])
                break

"""
"""
# 시간 초과
import sys

def is_prime_number(n):
    array = [True for i in range(n+1)] 
    for i in range(2, int(n**0.5) + 1): 
        if array[i] == True: 
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    return [ i for i in range(2, n+1) if array[i] ]

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    prime_num = is_prime_number(n)
    for j in range(-1, -len(prime_num)-1,-1):
        if prime_num[j] <= n//2:
            if n-prime_num[j] in prime_num:
                print(prime_num[j], n-prime_num[j])
                break

"""
# 메모리 29200KB, 시간 1856ms
import sys

array = [True] * 10001
for i in range(2, 101):
    if array[i] == True:
        for j in range(i+i, 10001, i):
            array[j] = False
prime_num = [i for i in range(2, 10001) if array[i] == True]

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    half = n//2
    for j in range(half, -1, -1):
        if j in prime_num and n-j in prime_num:
            print(j, n-j)
            break
