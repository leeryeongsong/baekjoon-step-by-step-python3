# https://www.acmicpc.net/problem/10757
# 푸는 중

A, B = input().split()
print(A)
print(B)
C = 0
result = ''

while len(A) != 0 and len(B) != 0:
    if len(A) >= 10:   
        A_num = int(A[-10:])
        print(A_num, 'A_num')
        A = A[:-10]
        print(A, 'A')
    else:
        A_num = int(A)
        A = ''
    if len(B) >= 10:
        B_num = int(B[-10:])
        print(B_num, 'b_num')
        B = B[:-10]
        print(B, 'B')
    else:
        B_num = int(B)
        B = ''
    result_num = str(A_num + B_num + C)
    print(result_num, 'result_num')
    C = 0
    if len(result_num) > 10:
        C = int(result_num[0])
        result = result_num[1:] + result
    else:
        result = result_num + result
print(result)
