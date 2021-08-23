# https://www.acmicpc.net/problem/1427

N = input()
N_list = list(map(int, N))
N_list.sort(reverse=True)
N_list = list(map(str, N_list))
result = ''.join(N_list)
print(result)
