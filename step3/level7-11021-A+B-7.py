# https://www.acmicpc.net/problem/11021
import sys

T = int(input())

for i in range(1, T+1):
  a, b = map(int, sys.stdin.readline().split())
  print("Case #{0}: {1}".format(i, a+b)) # 파이썬 문자열 포매팅 방법 중 format 함수 활용  
  # print("Case #%d: %d" %(i, a+b)) # 파이썬 문자열 포매팅 방법 중 % 포메팅 활용
  # print(f"Case #{i}:", a+b) # 파이썬 문자열 포매팅 방법 중 f-string 활용
