# https://www.acmicpc.net/problem/2292

N = int(input())

move = 1
endRoom = 1
gap = 0

while endRoom<N:
    move += 1
    gap += 6
    endRoom += gap

print(move)
