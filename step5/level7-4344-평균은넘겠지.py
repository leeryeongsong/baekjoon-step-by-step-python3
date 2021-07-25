# https://www.acmicpc.net/problem/4344

C = int(input())

for i in range(C):
    over_average_list = []
    N = list(map(int, input().split()))
    average = sum(N[1:])/N[0]
    for j in range(1, N[0]+1):
        if N[j]>average:
            over_average_list.append(N[j])
    over_average_student=len(over_average_list)/N[0]*100
    print(f"{over_average_student:.3f}%") # 문자열 포매팅 방법 f-string으로 소수점 자리수 조절하기
    # print("{:.3f}%".format(over_average_student)) # 문자열 포매팅 방법 str.format으로 소수점 자리수 조절하기
    # print(f"{round(over_average_student, 3)}%") # 이 문제에서는 round() 함수 사용 불가. 소수점 3자리수로 설정해도 40.0%으로 결과 나온다.
