# https://www.acmicpc.net/problem/2581

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

M = int(input())
N = int(input())
prime_num = [x for x in is_prime_number(N) if x not in is_prime_number(M-1)]

if len(prime_num) > 0:
    print(sum(prime_num))
    print(min(prime_num))
else:
    print(-1)
