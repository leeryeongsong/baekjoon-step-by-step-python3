# https://www.acmicpc.net/problem/1546

N = int(input())
score = list(map(int, input().split()))
new_score = [0 for i in range(N)]
# new_score = []이라고 하면, 리스트에 원소가 없는 상태에서 score[0] =1처럼 원소를 지정할 수 없으므로(IndexError: list assignment index out of range), 0을 N개 대입한다. 
M = max(score)

for i in range(N):
    new_score[i] = (score[i]/M)*100
average = sum(new_score)/N
print(average)



"""
N = int(input())
score = list(map(int, input().split()))
new_score = []
# new_score = []이라고 했으므로, 아래에 new_score.append(score[i]/M*100) 식을 사용했다.  
M = max(score)

for i in range(N):
    new_score.append(score[i]/M*100)
average = sum(new_score)/N
print(average)
"""
