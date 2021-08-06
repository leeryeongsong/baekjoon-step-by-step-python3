# https://www.acmicpc.net/problem/11653

N = int(input())
i = 2

if N > 1:
    while N > i:
        if N % i == 0:
            print(i)
            N = N // i
            continue
        else:
            i += 1
    print(N)
