# https://www.acmicpc.net/problem/1011

T = int(input())

for i in range(T):
    x, y = map(int, input().split())
    r = y - x
    k = 0
    count = 0
    gap = 1
    while k<r:
        k += gap
        count += 1
        if k>=r:
            print(count)
            break
        k += gap
        count += 1
        gap += 1
        if k>=r:
            print(count)
            break
