# https://www.acmicpc.net/problem/3052

a = []
for i in range(10):
  a.append(int(input()))
  a[i] = a[i]%42

a_set = set(a)
print(len(a_set))
