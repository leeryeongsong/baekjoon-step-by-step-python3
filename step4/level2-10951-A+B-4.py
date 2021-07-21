# https://www.acmicpc.net/problem/10951

"""
while True:
  a, b = map(int, input().split())
  print(a+b)
 런타임 에러(EOFError)

while True:
  a, b = map(int, input().split())
  if 0<a<10 and 0<b<10: 
    print(a+b)
  else:
    break
# 런타임 에러(EOFError)
"""

while True:
  try:
    a, b = map(int, input().split())
    print(a+b)
  except:
    break
