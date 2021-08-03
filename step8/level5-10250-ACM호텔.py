# https://www.acmicpc.net/problem/10250

T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    YY = N % H
    if YY == 0:
        YY = H
        XX = str(N //H)
    else:
        XX = str(N // H + 1)
    XX = XX.rjust(2, "0")
    print(f"{YY}{XX}")
