# https://www.acmicpc.net/problem/1978
# 에라토스테네스의 체 설명 https://velog.io/@koyo/python-is-prime-number

import math

def is_prime_number(n): # 에라토스테네스의 체
    array = [True for i in range(n+1)] 
    for i in range(2, int(math.sqrt(n)) + 1): 
        if array[i] == True: 
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    return [ i for i in range(2, n+1) if array[i] ]


N = int(input())
N_list = list(map(int, input().split()))
prime_num = is_prime_number(max(N_list))
count = 0

for i in N_list:
    if i in prime_num:
        count += 1

print(count)
