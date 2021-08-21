# https://www.acmicpc.net/problem/10989

import sys


def counting_sort(input_array, max):
    output_array= [-1]*len(input_array)
    counting_array = [0]*(max+1)
    for a in input_array:
        counting_array[a] += 1

    for i in range(max):
        counting_array[i+1] = counting_array[i]

    for j in input_array:
        output_array[counting_array[j]-1] = j
        counting_array[j] -= 1
    return output_array


N = int(sys.stdin.readline())
array = []
for i in range(N):
    x = int(sys.stdin.readline())
    array.append(x)
m = max(array)
print(m, 'm')
print(array, 'array')
output = counting_sort(array, m)
print(output,'output')
for j in range(N):
    print(output[j])
