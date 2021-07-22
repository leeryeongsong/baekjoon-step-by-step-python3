# https://www.acmicpc.net/problem/2562

N = []
Max = 0
MaxNum = 0
for i in range(9):
  N.append(int(input()))
for i in range(9):
  if Max==0 or Max<=N[i]:
    Max = N[i]
    MaxNum = i+1
  else:
    continue
print(Max)
print(MaxNum)
