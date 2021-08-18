# https://www.acmicpc.net/problem/1436

"""시행착오
import sys

N = int(sys.stdin.readline())
count = 1
i = 666

while count < N:
    i += 1
    i_list = list(str(i))
    for j in range(len(i_list)-2):
        if i_list[j] == '6' and i_list[j+1] == '6' and i_list[j+2] == '6':
            count += 1
        if count == N:
            break

print(i)

"""


# 메모리 29200KB 시간 3760ms	
import sys

N = int(sys.stdin.readline())
count = 1
i = 666

while count < N:
    i += 1
    end = 0
    i_list = list(str(i))
    for j in range(len(i_list)-2):
        if i_list[j] == '6' and i_list[j+1] == '6' and i_list[j+2] == '6':
            end = 1
    if end == 1:
        count += 1

print(i)
