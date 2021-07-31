# https://www.acmicpc.net/problem/1316

N = int(input())
count = N

for i in range(N):
    abc = []
    words=input()
    for j in range(len(words)):
        if words[j] not in abc:
            abc.append(words[j])
        else:
            if words[j-1]==words[j]:
                continue
            else:
                count -=1
                break

print(count)
