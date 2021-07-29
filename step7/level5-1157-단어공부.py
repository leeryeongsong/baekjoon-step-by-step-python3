# https://www.acmicpc.net/problem/1157

"""
# 메모리 31156KB 시간 404ms
words= input()
words_list = [0 for i in range(26)]

for i in words:
    if ord(i) <= 90:
        words_list[ord(i)-65] +=1
    else:
        words_list[ord(i)-97] +=1

words_list_max = max(words_list)

if words_list.count(words_list_max) == 1:
    words_list_max_index = words_list.index(words_list_max)
    print(chr(words_list_max_index+65))
else:
    print('?')

"""

"""
# 메모리 31156KB 시간 284ms
words= input().upper()

words_list = [0 for i in range(26)]

for i in words:
    words_list[ord(i)-65] +=1

words_list_max = max(words_list)
words_list_max_index = words_list.index(max(words_list))

if words_list.count(words_list_max) == 1:
    print(chr(words_list_max_index+65))
else:
    print('?')

"""

"""
# 시간 초과
words= input().upper()
words_list = [0 for i in range(26)]

for i in words:
    words_list[ord(i)-65] = words.count(i)

words_list_max = max(words_list)
words_list_max_index = words_list.index(max(words_list))

if words_list.count(words_list_max) == 1:
    print(chr(words_list_max_index+65))
else:
    print('?')

"""

"""
# 런타임 에러(TypeError)
words= input().upper()
words_set = set(words)
print(words_set)
words_fre = []

for i in words_set:
    words_fre.append(words.count(i))

if words_fre.count(max(words_fre)) == 1:
    print(words_set[words_fre.index(max(words_fre))]) # set 자료형은 순서가 없어서 인덱스가 없다.
else:
    print('?')
"""

"""
# 메모리 31156KB, 시간 120ms
words= input().upper()
words_set_list = list(set(words))
words_fre = []

for i in words_set_list:
    words_fre.append(words.count(i))

if words_fre.count(max(words_fre)) == 1:
    print(words_set_list[words_fre.index(max(words_fre))])
else:
    print('?')

"""

"""
# 메모리 31156KB, 시간 120ms
words= input().upper()
words_set_list = list(set(words))
words_fre = dict()


for i in words_set_list:
    words_fre[i] = words.count(i)
max_words_value = max(words_fre.values())
max_words = [key for key, value in words_fre.items() if value == max_words_value]

if len(max_words) == 1:
    print(max_words[0])
else:
    print('?')

"""
