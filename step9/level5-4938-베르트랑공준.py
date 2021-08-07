# https://www.acmicpc.net/problem/4948


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

n = 1
while n:
    n = int(input())
    if n == 0:
        break
    prime_num_2n = is_prime_number(2*n)
    prime_num_n = is_prime_number(n)
    print(len(prime_num_2n)-len(prime_num_n))

"""

# 메모리 34744KB 시간 4796 ms
import math
def is_prime_number_2n(n):
    array = [True for i in range(2*n+1)] 
    for i in range(2, int(math.sqrt(2*n)) + 1): 
        if array[i] == True: 
            j = 2
            while i * j <= 2*n:
                array[i * j] = False
                j += 1
    return [ i for i in range(n+1, 2*n+1) if array[i] ]

n = 1
while n:
    n = int(input())
    if n == 0:
        break
    print(len(is_prime_number_2n(n)))
