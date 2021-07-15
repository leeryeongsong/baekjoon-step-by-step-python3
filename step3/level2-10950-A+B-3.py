# https://www.acmicpc.net/problem/10950

T = int(input())
A = []
B = []
for i in range(T):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)
for j in range(T):
  print(int(A[j])+int(B[j]))
