# https://www.acmicpc.net/problem/2447


"""시행착오
N = int(input())
screen = [[" " for i in range(N)] for j in range(N)]

def star(N,screen):    
    if N == 3:
        screen = [
            ["*","*","*"], 
            ["*"," ","*"],
            ["*","*","*"]
            ]
        return screen

    for i in range(N//3):
        for j in range(N//3):
            if i != 2 and j != 2:
                screen[3*i:3*(i+1)][3*j:3*(j+1)] = star(N//3)
    return screen

star(N,screen)

for i in range(N):
    for j in range(N):
        print(screen[i][j], end='')
    print()

"""


"""시행착오

N = int(input())
screen = [["*" for i in range(N)] for j in range(N)]
print(screen)

def star(N,block):    
    if N == 3:
        block[1][1] = " "
        return block

    for i in range(N//3):
        for j in range(N//3):
            if i == 1 and j == 1:
                block[(N//3):(N//3)*2][(N//3):(N//3)*2] = [[" " for k in range(N//3)] for l in range(N//3)]
                print("if i == 1 and j == 1:screen[(N//3):(N//3)*2][(N//3):(N//3)*2] = " "")
                print(block[(N//3):(N//3)*2][(N//3):(N//3)*2])
            else:
                block[(N//3)*i:(N//3)*(i+1)][(N//3)*j:(N//3)*(j+1)] = star(N//3, [["*" for i in range(N//3)] for j in range(N//3)])
                print(" else:", block[(N//3)*i:(N//3)*(i+1)][(N//3)*j:(N//3)*(j+1)])
    return block

screen = star(N,screen)

for i in range(N):
    for j in range(N):
        print(screen[i][j], end='')
    print()


"""


"""테스트

N = [["*" for i in range(9)] for j in range(9)]
for i in range(9):
    for j in range(9):
        print(N[i][j], end='')
    print()


# 안 됨
#N[1:3][2:4] = " "

# 안 됨
# 2차원으로 리스트 인덱싱하여 2차원으로 리스트 값 설정할 수 없다.
# N[1:3][2:4] = [[" " for i in range(2)] for j in range(2)]

# 됨
# 한 줄씩 인덱싱 및 값 설정 가능.
N[1][2:4] = [" " for i in range(2)]

for i in range(9):
    for j in range(9):
        print(N[i][j], end='')
    print()

"""


# 메모리 67608KB, 시간 2828ms 
import sys

def star(N):    
    if N == 3:
        screen[1][:3] = ['*', ' ', '*']
        screen[0][:3] = screen[2][:3] = ['*']*3
        return
    

    star(N//3)

    for i in range(3):
        for j in range(3):
            if i != 1 or j != 1:
                for k in range(N//3):
                    screen[(N//3)*i+k][(N//3)*j:(N//3)*(j+1)] = screen[k][:(N//3)]


N = int(sys.stdin.readline())
screen = [[' ' for i in range(N)] for j in range(N)]


star(N)

for i in range(N):
    for j in range(N):
        print(screen[i][j], end='')
    print()
