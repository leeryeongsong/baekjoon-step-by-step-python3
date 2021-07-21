# https://www.acmicpc.net/problem/1110

N = int(input())
M = int
n = []
m = []
count = 0

if 0<=N<10:
  N = N*10

n = [N//10, N%10]

while N!=M:
  P = n[0]+n[1]  
  M = n[1]*10 + P%10
  n = [M//10, M%10]
  count+=1

print(count)
