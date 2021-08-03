# https://www.acmicpc.net/problem/

T = int(input())

for x in range(T):
    k = int(input())
    n = int(input())
    floor = list(range(1,15))

    for i in range(1, k+1):
        for N in range(1, 14):
            floor[N] = floor[N] + floor[N-1]
    print(floor[n-1])
