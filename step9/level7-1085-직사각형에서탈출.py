# https://www.acmicpc.net/problem/1085

x, y, w, h = map(int, input().split())

a = w - x
b = h - y
c = x
d = y
print(min(a, b, c, d))
