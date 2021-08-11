# https://www.acmicpc.net/problem/10872

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

N = int(input())
print(factorial(N))
