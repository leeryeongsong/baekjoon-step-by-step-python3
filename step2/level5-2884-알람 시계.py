# https://www.acmicpc.net/problem/2884

H, M = map(int, input().split())
if M>=45:
  print(H, M-45)
elif H==0:
  print("23", M+15)
else:
  print(H-1, M+15)
