# https://www.acmicpc.net/problem/2108

# 시간 초과
import sys

def average(array:list):
    ave = sum(array)//len(array)
    print(ave)

def medium(array:list):
    array.sort()
    print(array[len(array)//2])

def fre(array:list):
    array.sort()
    sorted_array = [x for x in array if x < 0] + [x for x in array if x>0]
    array_set_list = [x for x in set(sorted_array) if x < 0] + [x for x in set(sorted_array) if x>0]
    counting = []
    for i in array_set_list:
        counting.append(array.count(i))
    max_index = max(counting)
    max_list = []
    for j in range(len(counting)):
        if counting[j] == max_index:
            max_list.append(array_set_list[j])
    if len(max_list) > 1:
        print(max_list[1])
    else:
        print(max_list[0])

def ran(array:list):
    print(max(array)-min(array))


N = int(sys.stdin.readline())
array = []

for i in range(N):
    array.append(int(sys.stdin.readline()))

average(array)
medium(array)
fre(array)
ran(array)
