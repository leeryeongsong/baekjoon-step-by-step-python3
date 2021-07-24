# https://www.acmicpc.net/problem/8958

N = int(input())

for i in range(N):
    score = 0
    sum = 0
    test = input()
    test_list = list(test)
    for j in range(len(test_list)):
        if test_list[j] == "O":
            score += 1
        else: 
            score = 0
        sum += score    
    print(sum)
