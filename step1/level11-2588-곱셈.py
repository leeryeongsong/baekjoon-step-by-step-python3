# https://www.acmicpc.net/problem/2588

A = int(input())
B = input()
BB = []
for i in str(B):
  BB.append(i)
print(A*int(BB[2]))
print(A*int(BB[1]))
print(A*int(BB[0]))
print(A*int(BB[2])+10*A*int(BB[1])+100*A*int(BB[0]))
