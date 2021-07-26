# https://www.acmicpc.net/problem/1065

def is_it_hansu(x):
    x_list = list(map(int, str(x)))
    if len(x_list) <=2:
        return True
    else:
        d = x_list[1]-x_list[0]
        for i in range(2, len(x_list)):
            if d == x_list[i]-x_list[i-1]:
                continue
            else:
                return False
        return True

N = int(input())
hansu_list = []

for i in range(1, N+1):
    if is_it_hansu(i)==True:
        hansu_list.append(i)
    else:
        continue
print(len(hansu_list))
