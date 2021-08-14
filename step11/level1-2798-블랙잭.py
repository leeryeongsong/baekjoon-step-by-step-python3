# https://www.acmicpc.net/problem/2798

import sys

N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

blackjack = 0
sum = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = card[i] + card[j] + card[k]
            if sum > blackjack and sum <=M:
                blackjack = sum
print(blackjack)
