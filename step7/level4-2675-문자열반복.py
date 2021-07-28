# https://www.acmicpc.net/problem/2675

T = int(input())
for i in range(T):
    P = ''
    R, S = input().split()
    R = int(R)
    for j in range(len(S)):
        P = P + S[j]*R
    print(P)
