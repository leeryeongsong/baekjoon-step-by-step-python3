# https://www.acmicpc.net/problem/10809
"""
S = input()

for i in range(97, 123):
    if chr(i) not in S:
        print(-1, end = ' ')
    for j in range(len(S)):
        if chr(i)==S[j]:
            print(j, end = ' ')
            break
# 메모리 29200KB, 시간 80ms 코드 길이 193B
"""

S = input()

for i in range(97, 123):
    if chr(i) in S:
        for j in range(len(S)):
            if chr(i)==S[j]:
                print(j, end = ' ')
                break
    else:
        print(-1, end = ' ')

# 메모리 29200KB, 시간 80ms 코드 길이 215B   
