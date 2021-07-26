# https://www.acmicpc.net/problem/4673

"""
# set 사용하여 풀이. 시간이 더 짧게 나온다.
def d(n):
    n_list = list(map(int, str(n)))
    dn = n + sum(n_list)
    return dn

dn_set = set()

for i in range(1, 10001):
    dn_set.add(d(i))

for j in range(1, 10001):
    if j not in dn_set:
        print(j)

# 메모리 29968KB 시간 92ms 코드 길이 216B
"""
# list 사용하여 풀이. 시간이 더 길게 나온다.
def d(n):
    n_list = list(map(int, str(n)))
    dn = n + sum(n_list)
    return dn

dn_list = []

for i in range(1, 10001):
    if d(i) not in dn_list:
        dn_list.append(d(i))

for j in range(1, 10001):
    if j not in dn_list:
        print(j)
# 메모리 29452KB 시간 1144ms 코드 길이 251B
