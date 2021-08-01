
# 성공. 메모리 29200KB 시간 72ms 
A, B, C = map(int, input().split())

if B>=C:
    print(-1)
else:
    print(A//(C-B)+1)



"""
# 시행착오1
# 시간 초과

A, B, C = map(int, input().split())
count = 1

if B>=C:
    print(-1)
else:
    while A+B*count >= C*count:
        count += 1
    print(count)

"""

"""
# 시행착오2
# 시간 초과

A, B, C = map(int, input().split())
count = 1

if B>=C:
    print(-1)
else:
    cost = A + B
    earn = C
    while cost >= earn:
        count += 1
        cost += B
        earn += C
    print(count)
"""
