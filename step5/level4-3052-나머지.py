# https://www.acmicpc.net/problem/3052

a = []
for i in range(10):
  a.append(int(input()))
  a[i] = a[i]%42

a_set = set(a)
print(len(a_set))


# 순서가 중요할 경우, 반복문을 사용한다.
"""
a = []
new_a = []

for i in range(10):
  a.append(int(input()))
  a[i] = a[i]%42

for j in a:
  if j not in new_a:
    new_a.append(j)

print(len(new_a))
"""
