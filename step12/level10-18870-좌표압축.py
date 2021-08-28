# https://www.acmicpc.net/problem/18870

import sys

N = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().split()))

array_set = list(sorted(set(array)))

zip = {array_set[i] : i for i in range(len(array_set))}

for i in array:
    print(zip[i], end = ' ')
