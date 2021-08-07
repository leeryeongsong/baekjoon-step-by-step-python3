# https://www.acmicpc.net/problem/1929


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


M, N = map(int, input().split())
prime_num = [x for x in is_prime_number(N) if x not in is_prime_number(M-1)]
for i in range(len(prime_num)):
    print(prime_num[i])

"""

# 메모리 42488KB 시간 532ms 
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


M, N = map(int, input().split())
prime_num = is_prime_number(N)
for i in prime_num:
    if i>=M:
        print(i)
