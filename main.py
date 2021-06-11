#초기 설정
import numpy as np
import random
from wumpus import *
import turtle

percept_grid = [['' for col in range(4)] for row in range(4)] #초기 percept그리드
#wumpus_grid = [['' for col in range(4)]for row in range(4)]
#wumpus_grid[3][0] = wumpus_grid[2][0] = wumpus_grid[3][1] = 's'
user_grid = [['' for col in range(4)] for row in range(4)] #사용자가 게임을 하면서 현재 상태 정보 저장하는 그리드
percept_play_grid = [['' for col in range(4)] for row in range(4)] #게임을 하면서 쓰이는 percept 그리드. 초기 값은 percept_grid와 동일
visited_grid = [[ 0 for col in range(6)] for row in range(6)]
play_grid = [['' for col in range(4)] for row in range(4)] #게임을 하면서 쓰이는 wumpus grid. 초기 값은 wumpus_grid와 동일
dead_wumpus = [['' for col in range(4)] for row in range(4)]


#환경설정
#pitch wumpus
'''
for i in range(4):
    for j in range(4):
        if (i==3 and j == 0) or (i == 3 and j == 1) or (i == 2 and j == 0):
            continue
        else:
            a = random.choices(range(0,2), weights=[0.85, 0.15])
            if a == [1]:
                cnt_a += 1
                if cnt_a >= 3:
                    continue
                else:
                    wumpus_grid[i][j] += 'w'
                    percept_grid[i][j] += 's'

            b = random.choices(range(0,2), weights=[0.85, 0.15])
            if b == [1]:
                cnt_b += 1
                if cnt_b >= 3:
                    continue
                else:
                    wumpus_grid[i][j] += 'p'
                    percept_grid[i][j] += 'b'''''


#wumpus_grid[1][1] = wumpus_grid[1][1].replace('p','')
#percept_grid[1][1] = percept_grid[1][1].replace('p','')

#gold
'''=
breaker = False
while True:
    a = random.randint(0,3)
    b = random.randint(0,3)

    if (a == 0 and b == 0) or wumpus_grid[a][b].find('p') != -1 or wumpus_grid[a][b].find('w') != -1:
        a = random.randint(0,3)
        b = random.randint(0,3)

    else:
        wumpus_grid[a][b] += 'g'
        percept_grid[a][b] += 'g'
        break
'''

wumpus_grid = [[['','','','p'], ['','','',''],['g','','',''],['','','','w']],
               [['','','p',''], ['','g','','w'],['','','','p'],['','','','']],
               [['','p','w',''],['p','','g',''], ['','','',''],['','','','']],
               [['','','p',''], ['','','','g'], ['','','',''], ['','','w','']],
               [['','','','p'], ['','w','g','p'], ['','','w',''], ['','','','']],
               [['w','g','w',''], ['','','w','p'], ['','','p','p'], ['','','','']],
               [['','g','wp','p'], ['w','','',''], ['','','',''], ['','','','']],
               [['g','','','wp'], ['','w','',''], ['','p','',''], ['','','','']]]

a = random.randint(0,7)
print("a = ", a)
#a = 1

for i in range(4):
    print(wumpus_grid[a][i])

for i in range(4):
    for j in range(4):
        play_grid[i][j] = wumpus_grid[a][i][j]

drawWumpusTable(play_grid)

print("\n\n")
for i in range(4):
    print(play_grid[i])

#percept(glitter, stench, breeze)설정 함수
for i in range(4):
    for j in range(4):

        #gold
        if wumpus_grid[a][i][j].find('g') != -1:
            percept_grid[i][j] += 'g'


        #wumpus
        if wumpus_grid[a][i][j].find('w') != -1:
            percept_grid[i][j] += 's'
            if i == 0:
                percept_grid[i+1][j] += 's'
            elif i == 3:
                percept_grid[i-1][j] += 's'
            else:
                percept_grid[i-1][j] += 's'
                percept_grid[i+1][j] += 's'

            if j == 0:
                percept_grid[i][j+1] += 's'
            elif j == 3:
                percept_grid[i][j-1] += 's'
            else:
                percept_grid[i][j+1] += 's'
                percept_grid[i][j-1] += 's'

        #pitch
        if wumpus_grid[a][i][j].find('p') != -1:
            percept_grid[i][j] += 'b'
            if i == 0:
                percept_grid[i+1][j] += 'b'
            elif i == 3:
                percept_grid[i-1][j] += 'b'
            else:
                percept_grid[i-1][j] += 'b'
                percept_grid[i+1][j] += 'b'

            if j == 0:
                percept_grid[i][j+1] += 'b'
            elif j == 3:
                percept_grid[i][j-1] += 'b'
            else:
                percept_grid[i][j+1] += 'b'
                percept_grid[i][j-1] += 'b'


for i in range(4):
    for j in range(4):
        percept_play_grid[i][j] = percept_grid[i][j]

print("\n\n")
for i in range(4):
    print(percept_grid[i])

def visit():
    visited_grid = [[0 for col in range(6)] for row in range(6)]
    return visited_grid




#wumpus 죽이는거 성공했을 때 percet_play_grid에서 stench 지우는 함수
def delete_s(i, j, dir):
    if dir == 0:

        play_grid[3 - i][j + 1] = play_grid[3 - i][j + 1].replace('w', '', 1)
        percept_play_grid[3 - i][j + 1] = percept_play_grid[3 - i][j + 1].replace('s', '', 1)

        if 3 - i >= 1 and 3 - i <= 2 and j + 1 >= 1 and j + 1 <= 2:
            percept_play_grid[3 - i - 1][j + 1] = percept_play_grid[3 - i - 1][j + 1].replace('s', '', 1)
            percept_play_grid[3 - i + 1][j + 1] = percept_play_grid[3 - i + 1][j + 1].replace('s', '', 1)
            percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
            percept_play_grid[3 - i][j + 2] = percept_play_grid[3 - i][j + 2].replace('s', '', 1)

        elif 3 - i == 0:
            if j + 1 == 3:
                percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
                percept_play_grid[3 - i + 1][j + 1] = percept_play_grid[3 - i + 1][j + 1].replace('s', '', 1)
            else:
                percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
                percept_play_grid[3 - i + 1][j + 1] = percept_play_grid[3 - i + 1][j + 1].replace('s', '', 1)
                percept_play_grid[3 - i][j + 2] = percept_play_grid[3 - i][j + 2].replace('s', '', 1)

        elif 3 - i == 3:
            if j + 1 == 3:
                percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
                percept_play_grid[3 - i - 1][j + 1] = percept_play_grid[3 - i - 1][j + 1].replace('s', '', 1)
            else:
                percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
                percept_play_grid[3 - i - 1][j + 1] = percept_play_grid[3 - i - 1][j + 1].replace('s', '', 1)
                percept_play_grid[3 - i][j + 2] = percept_play_grid[3 - i][j + 2].replace('s', '', 1)

        else:
            percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
            percept_play_grid[3 - i - 1][j + 1] = percept_play_grid[3 - i - 1][j + 1].replace('s', '', 1)
            percept_play_grid[3 - i + 1][j + 1] = percept_play_grid[3 - i + 1][j + 1].replace('s', '', 1)


    if dir == 1:
        play_grid[3 - i + 1][j] = play_grid[3 - i + 1][j].replace('w', '')
        percept_play_grid[3 - i + 1][j] = percept_play_grid[3 - i + 1][j].replace('s', '', 1)

        if 3 - i + 1 >= 1 and 3 - i + 1 <= 2 and j >= 1 and j <= 2:
            percept_play_grid[3 - i + 1][j - 1] = percept_play_grid[3 - i + 1][j - 1].replace('s', '', 1)
            percept_play_grid[3 - i + 2][j] = percept_play_grid[3 - i + 2][j].replace('s', '', 1)
            percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
            percept_play_grid[3 - i + 1][j + 1] = percept_play_grid[3 - i + 1][j + 1].replace('s', '', 1)

        elif 3 - i == 0:
            if j == 3:
                percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
                percept_play_grid[3 - i + 1][j - 1] = percept_play_grid[3 - i + 1][j - 1].replace('s', '', 1)
                percept_play_grid[3 - i + 2][j] = percept_play_grid[3 - i + 2][j].replace('s', '', 1)
            elif j == 0:
                percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
                percept_play_grid[3 - i + 1][j + 1] = percept_play_grid[3 - i + 1][j + 1].replace('s', '', 1)
                percept_play_grid[3 - i + 2][j] = percept_play_grid[3 - i + 2][j].replace('s', '', 1)

        elif 3 - i + 1 == 3:
            if j == 3:
                percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
                percept_play_grid[3 - i + 1][j - 1] = percept_play_grid[3 - i + 1][j - 1].replace('s', '', 1)
            else:
                percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
                percept_play_grid[3 - i + 1][j - 1] = percept_play_grid[3 - i + 1][j - 1].replace('s', '', 1)
                percept_play_grid[3 - i + 1][j + 1] = percept_play_grid[3 - i + 1][j + 1].replace('s', '', 1)

        else:
            percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
            percept_play_grid[3 - i + 1][j - 1] = percept_play_grid[3 - i + 1][j - 1].replace('s', '', 1)
            percept_play_grid[3 - i + 2][j] = percept_play_grid[3 - i + 2][j].replace('s', '', 1)


    if dir == 2:

        play_grid[3 - i][j - 1] = play_grid[3 - i][j - 1].replace('w', '')
        percept_play_grid[3 - i][j - 1] = percept_play_grid[3 - i][j - 1].replace('s', '', 1)

        if 3 - i >= 1 and 3 - i <= 2 and j - 1 >= 1 and j - 1 <= 2:
            percept_play_grid[3 - i - 1][j - 1] = percept_play_grid[3 - i - 1][j - 1].replace('s', '', 1)
            percept_play_grid[3 - i + 1][j - 1] = percept_play_grid[3 - i + 1][j - 1].replace('s', '', 1)
            percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
            percept_play_grid[3 - i][j - 2] = percept_play_grid[3 - i][j - 2].replace('s', '', 1)

        elif 3 - i == 0:
            if j - 1 == 0:
                percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
                percept_play_grid[3 - i + 1][j - 1] = percept_play_grid[3 - i + 1][j - 1].replace('s', '', 1)
            else:
                percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
                percept_play_grid[3 - i + 1][j - 1] = percept_play_grid[3 - i + 1][j - 1].replace('s', '', 1)
                percept_play_grid[3 - i][j - 2] = percept_play_grid[3 - i][j - 2].replace('s', '', 1)

        elif 3 - i == 3:
            percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
            percept_play_grid[3 - i][j - 2] = percept_play_grid[3 - i][j - 2].replace('s', '', 1)
            percept_play_grid[3 - i - 1][j - 1] = percept_play_grid[3 - i - 1][j - 1].replace('s', '', 1)

        else:
            percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
            percept_play_grid[3 - i - 1][j - 1] = percept_play_grid[3 - i - 1][j - 1].replace('s', '', 1)
            percept_play_grid[3 - i + 1][j - 1] = percept_play_grid[3 - i + 1][j - 1].replace('s', '', 1)


    if dir == 3:
        play_grid[3 - i - 1][j] = play_grid[3 - i - 1][j].replace('w', '')
        percept_play_grid[3 - i - 1][j] = percept_play_grid[3 - i - 1][j].replace('s', '', 1)

        if 3 - i - 1 >= 1 and 3 - i - 1 <= 2 and j >= 1 and j <= 2:
            percept_play_grid[3 - i - 1][j - 1] = percept_play_grid[3 - i - 1][j - 1].replace('s', '', 1)
            percept_play_grid[3 - i - 1][j + 1] = percept_play_grid[3 - i - 1][j + 1].replace('s', '', 1)
            percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
            percept_play_grid[3 - i - 2][j] = percept_play_grid[3 - i - 2][j].replace('s', '', 1)


        elif 3 - i - 1== 0:
            if j == 0:
                percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
                percept_play_grid[3 - i - 1][j + 1] = percept_play_grid[3 - i - 1][j + 1].replace('s', '', 1)

            elif j == 3:
                percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
                percept_play_grid[3 - i - 1][j - 1] = percept_play_grid[3 - i - 1][j - 1].replace('s', '', 1)

            else:
                percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
                percept_play_grid[3 - i - 1][j - 1] = percept_play_grid[3 - i - 1][j - 1].replace('s', '', 1)
                percept_play_grid[3 - i - 1][j + 1] = percept_play_grid[3 - i - 1][j + 1].replace('s', '', 1)

        elif 3 - i -1 == 1:
            if j == 0:
                percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
                percept_play_grid[3 - i - 1][j + 1] = percept_play_grid[3 - i - 1][j + 1].replace('s', '', 1)
                percept_play_grid[3 - i - 2][j] = percept_play_grid[3 - i - 2][j].replace('s', '', 1)
            elif j == 3:
                percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
                percept_play_grid[3 - i - 1][j - 1] = percept_play_grid[3 - i - 1][j - 1].replace('s', '', 1)
                percept_play_grid[3 - i - 2][j] = percept_play_grid[3 - i - 2][j].replace('s', '', 1)

        else:
            percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('s', '', 1)
            percept_play_grid[3 - i - 2][j] = percept_play_grid[3 - i - 2][j].replace('s', '', 1)
            percept_play_grid[3 - i - 1][j - 1] = percept_play_grid[3 - i - 1][j - 1].replace('s', '', 1)



#stench가 느껴지면 화살 쏘는 함수
def shoot_w(i, j, dir):
    if dir == 0:
        if play_grid[3 - i][j + 1].find('w') != -1:
            alertScream()
            if user_grid[3-i][j+1].find('w') == -1:
                user_grid[3 - i][j+1] += 'w'
            dead_wumpus[3-i][j+1] += 'w'
            play_grid[3 - i][j + 1] = play_grid[3 - i][j + 1].replace('w', '', 1)
            percept_play_grid[3 - i][j + 1] = percept_play_grid[3 - i][j + 1].replace('s', '', 1)
            delete_s(i,j,dir)
        else:
            alertShoot()

    if dir == 1:
        if play_grid[3-i+1][j].find('w') != -1:
            alertScream()
            if user_grid[3 - i +1][j].find('w') == -1:
                user_grid[3-i+1][j] += 'w'
            dead_wumpus[3-i+1][j] += 'w'
            play_grid[3-i+1][j] = play_grid[3 - i + 1][j].replace('w', '')
            percept_play_grid[3-i+1][j] = percept_play_grid[3-i+1][j].replace('s', '', 1)
            delete_s(i,j,dir)
        else:
            alertShoot()

    if dir == 2:
        if play_grid[3 - i][j - 1].find('w') != -1:
            alertScream()
            if user_grid[3 - i][j - 1].find('w') == -1:
                user_grid[3 - i][j -1] += 'w'
            dead_wumpus[3-i][j-1] += 'w'
            play_grid[3 - i][j - 1] = play_grid[3 - i][j - 1].replace('w', '')
            percept_play_grid[3 - i][j - 1] = percept_play_grid[3 - i][j - 1].replace('s', '', 1)
            delete_s(i,j,dir)
        else:
            alertShoot()

    if dir == 3:
        if play_grid[3 - i - 1][j].find('w') != -1:
            alertScream()
            if user_grid[3 - i - 1][j].find('w') == -1:
                user_grid[3 - i -1][j] += 'w'
            dead_wumpus[3-i-1][j] += 'w'
            play_grid[3 - i - 1][j] = play_grid[3 - i - 1][j].replace('w', '')
            percept_play_grid[3 - i - 1][j] = percept_play_grid[3 - i - 1][j].replace('s', '', 1)
            delete_s(i, j, dir)
        else:
            alertShoot()

def delete_g(i,j,dir):

    play_grid[3 - i][j] = play_grid[3 - i][j].replace('g', '', 1)
    percept_play_grid[3 - i][j] = percept_play_grid[3 - i][j].replace('g', '', 1)

    if 3 - i >= 1 and 3 - i <= 2 and j >= 1 and j <= 2:
        percept_play_grid[3 - i - 1][j] = percept_play_grid[3 - i - 1][j].replace('g', '', 1)
        percept_play_grid[3 - i + 1][j] = percept_play_grid[3 - i + 1][j] .replace('g', '', 1)
        percept_play_grid[3 - i][j - 1] = percept_play_grid[3 - i][j - 1].replace('g', '', 1)
        percept_play_grid[3 - i][j + 1] = percept_play_grid[3 - i][j + 1].replace('g', '', 1)

    elif 3 - i == 0:
        if j == 3:
            percept_play_grid[3 - i][j - 1] = percept_play_grid[3 - i][j - 1].replace('g', '', 1)
            percept_play_grid[3 - i + 1][j] = percept_play_grid[3 - i + 1][j].replace('g', '', 1)
        elif j == 0:
            percept_play_grid[3 - i + 1][j] = percept_play_grid[3 - i + 1][j].replace('g', '', 1)
            percept_play_grid[3 - i][j + 1] = percept_play_grid[3 - i][j + 1].replace('g', '', 1)
        else:
            percept_play_grid[3-i][j-1] = percept_play_grid[3-i][j-1].replace('g','',1)
            percept_play_grid[3-i][j+1] = percept_play_grid[3-i][j+1].replace('g','',1)
            percept_play_grid[3-i+1][j] = percept_play_grid[3-i+1][j].replace('g','',1)

    elif 3 - i == 3:
        if j == 3:
            percept_play_grid[3 - i - 1][j] = percept_play_grid[3 - i - 1][j].replace('g', '', 1)
            percept_play_grid[3 - i][j - 1] = percept_play_grid[3 - i][j - 1].replace('g', '', 1)
        else:
            percept_play_grid[3 - i - 1][j] = percept_play_grid[3 - i - 1][j].replace('g', '', 1)
            percept_play_grid[3 - i][j + 1] = percept_play_grid[3 - i][j + 1].replace('g', '', 1)
            percept_play_grid[3 - i][j - 1] = percept_play_grid[3 - i][j - 1].replace('g', '', 1)

    else:
        if j == 0:
            percept_play_grid[3 - i - 1][j] = percept_play_grid[3 - i - 1][j].replace('g', '', 1)
            percept_play_grid[3 - i][j + 1] = percept_play_grid[3 - i][j + 1].replace('g', '', 1)
            percept_play_grid[3 - i + 1][j] = percept_play_grid[3 - i + 1][j].replace('g', '', 1)
        elif j == 3:
            percept_play_grid[3-i-1][j] = percept_play_grid[3-i-1][j].replace('g','',1)
            percept_play_grid[3-i][j-1] = percept_play_grid[3-i][j-1].replace('g','',1)
            percept_play_grid[3-i+1][j] = percept_play_grid[3-i+1][j].replace('g','',1)





i = 0
j = 0
dir = 0
shoot = 3

drawTurtle()
while (True):
    play_1 = 0
    i = 0
    j = 0
    dir = 0
    #방문 배열 초기화
    visited_grid = [[0 for col in range(6)] for row in range(6)]
    #kb 출력
    for s in range(4):
        print(user_grid[s])
    #현재 상태 저장하는 배열 초기화
    for q in range(4):
        for p in range(4):
            play_grid[q][p] = wumpus_grid[a][q][p]
    #현재 퍼셉트 저장하는 배열 초기화
    for q in range(4):
        for p in range(4):
            percept_play_grid[q][p] = percept_grid[q][p]

    shoot = 3
    gold = 0
    visited_x = []
    visited_y = []

    while (True):
        problem = 0

        play_1 +=1
        i, j, x, y = drawGoForward(i, j, dir)
        print("\n-----------시도 횟수:", play_1,"--------------")
        print('현재 위치: i = ',i, 'j = ',j, "\n")
        print("현재 방향: ", dir)
        print("격자 위치: x = ",x, "y = ", y, "\n" )
        print("gold = ", gold)

        visited_x.append(i)
        visited_y.append(j)

        #bump_구석
        if (i == 4 and j == 0):
            del visited_x[-1]
            del visited_y[-1]
            alertBump()
            dir = drawTurnRight(dir)
            print("dir = ", dir)
            i -= 1
            print("회전 후  i = ", i, ", j = ", j)

        elif (i == 3 and j == -1):
            del visited_x[-1]
            del visited_y[-1]
            alertBump()
            dir = drawTurnLeft(dir)
            print("dir = ", dir)
            j+=1
            print("회전 후  i = ", i, ", j = ", j)
        elif (i == 4 and j == 3):
            del visited_x[-1]
            del visited_y[-1]
            alertBump()
            dir = drawTurnLeft(dir)
            print("dir = ", dir)
            i-=1
            print("회전 후  i = ", i, ", j = ", j)
        elif (i==3 and j==4):
            del visited_x[-1]
            del visited_y[-1]
            alertBump()
            dir = drawTurnRight(dir)
            print("dir = ", dir)
            j-=1
            print("회전 후  i = ", i, ", j = ", j)
        elif(i==0 and j==4):
            del visited_x[-1]
            del visited_y[-1]
            alertBump()
            dir = drawTurnLeft(dir)
            print("dir = ", dir)
            j-=1
            print("회전 후  i = ", i, ", j = ", j)
        elif(i==-1 and j==3):
            del visited_x[-1]
            del visited_y[-1]
            alertBump()
            dir = drawTurnRight(dir)
            print("dir = ", dir)
            i+=1
            print("회전 후  i = ", i, ", j = ", j)

        #bump
        if (i == -1 and ( j == 1 or j ==2)):
            del visited_x[-1]
            del visited_y[-1]
            alertBump()
            dir = randomdir(dir)
            print("dir = ", dir)
            i+=1
            print("회전 후  i = ",i, ", j = ", j)
        if (i == 4 and (j == 1 or j == 2)):
            del visited_x[-1]
            del visited_y[-1]
            alertBump()
            dir = randomdir(dir)
            print("dir = ", dir)
            i-=1
            print("회전 후  i = ", i, ", j = ", j)
        if (j == -1 and (i == 1 or i == 2)):
            del visited_x[-1]
            del visited_y[-1]
            alertBump()
            dir = randomdir(dir)
            print("dir = ", dir)
            j+=1
            print("회전 후  i = ",i, ", j = ", j)
        if (j==4 and  (i == 1 or i ==2)):
            del visited_x[-1]
            del visited_y[-1]
            alertBump()
            dir = randomdir(dir)
            print("dir = ", dir)
            j-=1
            print("회전 후  i = ", i, ", j = ", j)

        #현재 위치에 wumpus가 있다면 죽음
        if (play_grid[3-i][j].find('w') != -1):
            user_grid[3-i][j] += 'w'
            print("[wumpus] You die")
            alertWumpusDie()
            clearTurtle()
            break

        #현재 위치에 pit가 있다면 죽음
        if (play_grid[3-i][j].find('p') != -1):
            user_grid[3-i][j] += 'p'
            print("[pit] You die")
            alertPitDie()
            clearTurtle()
            break

        # glitter가 느껴지면 gold += 1
        if percept_play_grid[3 - i][j].find('g') != -1:
            alertGlitter()
            if play_grid[3 - i][j].find('g') != -1:
                gold += 1
                print("\nYou find gold!\n")
                delete_g(i, j, dir)
                user_grid[3 - i][j] += 'g'
            else:
                print("실패!")
                alertFailGrab()


        if gold == 0:
            if i == 1 and j == 0:
                if dir == 1:
                    dir = drawTurnLeft(dir)
            elif i == 0 and j == 1:
                if dir == 2:
                    dir = drawTurnRight(dir)
                    print(dir)

        visit_len = len(visited_x)
        print("visit len = ", visit_len)
        s1 = visit_len - 2
        s2 = visit_len - 2

        if gold == 1:
            alertSuccessGrab()
            clearTurtle()
            drawBackward(visit_len, visited_x, visited_y)
            drawUserTable(user_grid, shoot)
            break;

        #pit&wumpus
        if dir == 0:
            if not (j == 3): #내 진행방향에
                if user_grid[3 - i][j + 1].find('w') != -1: #웜퍼스 있는거 알아
                    if dead_wumpus[3-i][j+1].find('w') == -1: #근데아직 안죽임
                        if shoot > 0:
                            shoot -= 1
                            print("\nremaining shoot is ", shoot, "\n")
                            alertScream()
                            delete_s(i, j, dir)
                        else:
                            alertShoot()
                            print("\nremaining shoot is ", shoot, "\n")

                else: #웜퍼스 있는거 모르는데
                    if percept_play_grid[3 - i][j].find('s') != -1: #내 자리에서 s느껴져
                        print("I can feel s in (", i, j, ")\n")
                        alertStench()
                        if i == 3:
                            if user_grid[3 - i + 1][j].find('w') != -1:  # 내 오른쪽에 웜퍼스 있는거 알아
                                if dead_wumpus[3-i+1][j].find('w') == -1:
                                    if shoot > 0:
                                        dir = drawTurnRight(dir)
                                        shoot -= 1
                                        print("\nremaining shoot is ", shoot, "\n")
                                        alertScream()
                                        delete_s(i, j, dir)
                                    else:
                                        alertShoot()
                                        print("remaining shoot is ", shoot, "\n")
                            else:
                                if shoot > 0:
                                    shoot -= 1
                                    print("\nremaining shoot is ", shoot, "\n")
                                    shoot_w(i, j, dir)
                                else:
                                    alertShoot()
                                    print("remaining shoot is ", shoot, "\n")

                        elif i == 0:
                            if user_grid[3 - i - 1][j].find('w') != -1: # 내 왼쪽에 있는걸 알아
                                if dead_wumpus[3-i-1][j].find('w') == -1:
                                    if shoot > 0:
                                        dir = drawTurnLeft(dir)
                                        shoot -= 1
                                        print("\nremaining shoot is ", shoot, "\n")
                                        alertScream()
                                        delete_s(i, j, dir)
                                    else:
                                        alertShoot()
                                        print("remaining shoot is ", shoot, "\n")
                            else:
                                if shoot > 0:
                                    shoot -= 1
                                    print("\nremaining shoot is ", shoot, "\n")
                                    shoot_w(i, j, dir)
                                else:
                                    alertShoot()
                                    print("remaining shoot is ", shoot, "\n")

                        else:
                            if user_grid[3 - i - 1][j].find('w') != -1: # 내 왼쪽에 있는걸 알아
                                if dead_wumpus[3-i-1][j].find('w') == -1:
                                    if shoot > 0:
                                        dir = drawTurnLeft(dir)
                                        shoot -= 1
                                        print("\nremaining shoot is ", shoot, "\n")
                                        alertScream()
                                        delete_s(i, j, dir)
                                    else:
                                        alertShoot()
                                        print("remaining shoot is ", shoot, "\n")

                            elif user_grid[3 - i + 1][j].find('w') != -1:  # 내 오른쪽에 웜퍼스 있는거 알아
                                if dead_wumpus[3-i+1][j].find('w') == -1:
                                    if shoot > 0:
                                        dir = drawTurnRight(dir)
                                        shoot -= 1
                                        print("\nremaining shoot is ", shoot, "\n")
                                        alertScream()
                                        delete_s(i, j, dir)
                                    else:
                                        alertShoot()
                                        print("remaining shoot is ", shoot, "\n")
                            else: #모르면 그냥 진행 방향 쪽으로
                                if shoot > 0:
                                    shoot -= 1
                                    print("\nremaining shoot is ", shoot, "\n")
                                    shoot_w(i, j, dir)
                                else:
                                    alertShoot()
                                    print("remaining shoot is ", shoot, "\n")


                if user_grid[3-i][j+1].find('p') != -1: #피트가 있는거 알아
                    if (i == 0):
                        if user_grid[3-i-1][j].find('p') == -1:
                            dir = drawTurnLeft(dir)
                        else:
                            dir = drawTurnLeft(dir)
                            dir = drawTurnLeft(dir)
                    elif (i == 3):
                        if user_grid[3-i+1][j].find('p') == -1:
                            dir = drawTurnRight(dir)
                        else:
                            dir = drawTurnRight(dir)
                            dir = drawTurnRight(dir)
                    else:
                        if user_grid[3-i-1][j].find('p') == -1 and user_grid[3-i+1][j].find('p') == -1:
                            dir = randomdir(dir)
                        elif user_grid[3-i-1][j].find('p') != -1 and user_grid[3-i+1][j].find('p') == -1:
                            dir = drawTurnRight(dir)
                        elif user_grid[3-i-1][j].find('p') == -1 and user_grid[3-i+1][j].find('p') != -1:
                            dir = drawTurnLeft(dir)
                        else:
                            dir = drawTurnRight(dir)
                            dir = drawTurnRight(dir)
                else: #피트가 있는거 모르는데
                    if percept_play_grid[3-i][j].find('b') != -1: #b느껴져
                        print("I can feel b in (",i,j,")\n")
                        alertBreeze()
                        if (i==0):
                            if user_grid[3-i-1][j].find('p') == -1:
                                dir = drawTurnLeft(dir)
                        elif (i==3):
                            if user_grid[3-i+1][j].find('p') == -1:
                                dir = drawTurnRight(dir)
                        else:
                            if user_grid[3-i+1][j].find('p') == -1 and user_grid[3-i-1][j].find('p')==-1:
                                dir = randomdir(dir)
                            elif user_grid[3-i+1][j].find('p') != -1 and user_grid[3-i-1][j].find('p') == -1:
                                dir = drawTurnLeft(dir)
                            elif user_grid[3-i-1][j].find('p') != -1 and user_grid[3-i+1][j].find('p') == -1:
                                dir = drawTurnRight(dir)
            else: #현재 내 자리에
                if percept_play_grid[3 - i][j].find('b') != -1:
                    print("I can feel b in (", i, j, ")\n")
                    alertBreeze()
                    if (i == 0):
                        if user_grid[3-i-1][j].find('p') == -1:
                            dir = drawTurnLeft(dir)
                        else:
                            dir = drawTurnLeft(dir)
                            dir = drawTurnLeft(dir)
                    elif (i == 3):
                        if user_grid[3-i+1][j].find('p') == -1:
                            dir = drawTurnRight(dir)
                        else:
                            dir = drawTurnRight(dir)
                            dir = drawTurnRight(dir)
                    else:
                        if user_grid[3-i-1][j].find('p') == -1 and user_grid[3-i+1][j].find('p') == -1:
                            dir = randomdir(dir)
                        elif user_grid[3-i-1][j].find('p') != -1 and user_grid[3-i+1][j].find('p') == -1:
                            dir = drawTurnRight(dir)
                        elif user_grid[3-i-1][j].find('p') == -1 and user_grid[3-i+1][j].find('p') != -1:
                            dir = drawTurnLeft(dir)
                        else:
                            dir = drawTurnRight(dir)
                            dir = drawTurnRight(dir)

        elif dir == 1:
            if not (i == 0): #현재 내 진행 방향에
                if user_grid[3 - i + 1][j].find('w') != -1: #웜퍼스 있는거 알아
                    if dead_wumpus[3-i+1][j].find('w') == -1: #근데 아직 안죽임
                        if shoot > 0: #슛이 있다면
                            shoot -= 1
                            print("\nremaining shoot is ", shoot, "\n")
                            alertScream()
                            delete_s(i, j, dir)
                        else: #슛이 없다면
                            alertShoot()
                            print("\nremaining shoot is ", shoot, "\n")
                else: #있는거 몰라
                    if percept_play_grid[3 - i][j].find('s') != -1: #근데 s가 느껴져
                        print("I can feel s in (", i, j, ")\n")
                        alertStench()
                        if j == 3:
                            if user_grid[3-i][j-1].find('w') != -1: #내 오른쪽에 웜퍼스 있는거 알아
                                if dead_wumpus[3-i][j-1].find('w') == -1:
                                    if shoot > 0:  # 슛이 있다면 쏴
                                        dir = drawTurnRight(dir)
                                        shoot -= 1
                                        print("\nremaining shoot is ", shoot, "\n")
                                        shoot_w(i, j, dir)
                                    else:  # 없으면 못쏴
                                        alertShoot()
                                        print("\nremaining shoot is ", shoot, "\n")
                            else:
                                if shoot > 0:
                                    shoot -= 1
                                    print("\nremaining shoot is ", shoot, "\n")
                                    shoot_w(i, j, dir)
                                else:
                                    alertShoot()
                                    print("remaining shoot is ", shoot, "\n")
                        elif j == 0:
                            if user_grid[3-i][j+1].find('w') != -1: #내 왼쪽에 있는걸 알아
                                if dead_wumpus[3-i][j+1].find('w') == -1:
                                    if shoot > 0:  # 슛이 있다면 쏴
                                        dir = drawTurnLeft(dir)
                                        shoot -= 1
                                        print("\nremaining shoot is ", shoot, "\n")
                                        shoot_w(i, j, dir)
                                    else:  # 없으면 못쏴
                                        alertShoot()
                                        print("\nremaining shoot is ", shoot, "\n")
                            else:
                                if shoot > 0:
                                    shoot -= 1
                                    print("\nremaining shoot is ", shoot, "\n")
                                    shoot_w(i, j, dir)
                                else:
                                    alertShoot()
                                    print("remaining shoot is ", shoot, "\n")
                        else:
                            if user_grid[3-i][j+1].find('w') != -1: #내 왼쪽에 있는걸 알아
                                if dead_wumpus[3-i][j+1].find('w') == -1:
                                    if shoot > 0:  # 슛이 있다면 쏴
                                        dir = drawTurnLeft(dir)
                                        shoot -= 1
                                        print("\nremaining shoot is ", shoot, "\n")
                                        shoot_w(i, j, dir)
                                    else:  # 없으면 못쏴
                                        alertShoot()
                                        print("\nremaining shoot is ", shoot, "\n")

                            elif user_grid[3-i][j-1].find('w')!= -1:
                                if dead_wum[3-i][j-1].find('w') == -1:
                                    if shoot > 0:
                                        dir = drawTurnRight(dir)
                                        shoot -= 1
                                        print("\nremaining shoot is ", shoot, "\n")
                                        shoot_w(i,j,dir)
                                    else:
                                        alertShoot()
                                        print("\nremaining shoot is ", shoot,"\n")
                            else:
                                if shoot > 0:
                                    shoot -= 1
                                    print("\nremaining shoot is ", shoot, "\n")
                                    shoot_w(i, j, dir)
                                else:
                                    alertShoot()
                                    print("remaining shoot is ", shoot, "\n")


                if user_grid[3 - i + 1][j].find('p') != -1:
                    if j == 0:
                        dir = drawTurnLeft(dir)
                    elif j == 3:
                        if user_grid[3 - i][j - 1].find('p') == -1:
                            dir = drawTurnRight(dir)
                        else:
                            dir = drawTurnRight(dir)
                            dir = drawTurnRight(dir)
                    else:
                        if user_grid[3 - i][j - 1].find('p') == -1 and user_grid[3 - i][j + 1].find('p') == -1:
                            dir = randomdir(dir)
                        elif user_grid[3 - i][j - 1].find('p') != -1 and user_grid[3 - i][j + 1].find('p') == -1:
                            dir = drawTurnLeft(dir)
                        elif user_grid[3 - i][j - 1].find('p') == -1 and user_grid[3 - i][j + 1].find('p') != -1:
                            dir = drawTurnRight(dir)
                        else:
                            dir = drawTurnRight(dir)
                            dir = drawTurnRight(dir)
                else:
                    if percept_play_grid[3 - i][j].find('b') != -1:
                        print("I can feel b in (", i, j, ")\n")
                        alertBreeze()
                        if j == 0:
                            if user_grid[3 - i][j + 1].find('p') == -1:
                                dir = drawTurnLeft(dir)
                        elif j == 3:
                            if user_grid[3 - i][j - 1].find('p') == -1:
                                dir = drawTurnRight(dir)
                        else:
                            if user_grid[3 - i][j - 1].find('p') == -1 and user_grid[3 - i][j + 1].find('p') == -1:
                                dir = randomdir(dir)
                            elif user_grid[3 - i][j - 1].find('p') != -1 and user_grid[3 - i][j + 1].find('p') == -1:
                                dir = drawTurnLeft(dir)
                            elif user_grid[3 - i][j - 1].find('p') == -1 and user_grid[3 - i][j + 1].find('p') != -1:
                                dir = drawTurnRight(dir)

            else: #현재 내 자리에서
                if percept_play_grid[3 - i][j].find('b') != -1:
                    print("I can feel b in (", i, j, ")\n")
                    alertBreeze()
                    if j == 3:
                        if user_grid[3-i][j-1].find('p') == -1:
                            dir = drawTurnRight(dir)
                        else:
                            dir = drawTurnRight(dir)
                            dir = drawTurnRight(dir)
                    else:
                        if user_grid[3-i][j-1].find('p') == -1 and user_grid[3-i][j+1].find('p') == -1:
                            dir = randomdir(dir)
                        elif user_grid[3-i][j-1].find('p') != -1 and user_grid[3-i][j+1].find('p') == -1:
                            dir = drawTurnLeft(dir)
                        else:
                            dir = drawTurnRight(dir)
                            dir = drawTurnRight(dir)

        elif dir == 2:
            if not (j == 0): # 내 진행 방향에
                if user_grid[3 - i][j - 1].find('w') != -1: #웜퍼스가 있는걸 알아
                    if dead_wumpus[3-i][j-1].find('w') == -1: #근데 안죽인 웜퍼스
                        if shoot > 0:
                            shoot -= 1
                            print("\nremaining shoot is ", shoot, "\n")
                            alertScream()
                            delete_s(i, j, dir)
                        else:
                            alertShoot()
                            print("\nremaining shoot is ", shoot, "\n")
                else: #모르는데
                    if percept_play_grid[3 - i][j].find('s') != -1: #s가 느껴져
                        print("I can feel s in (", i, j, ")\n")
                        alertStench()
                        if i == 0:
                            if user_grid[3-i+1][j].find('w') != -1: #내 왼쪽에 웜퍼스 있음
                                if dead_wumpus[3-i][j-1].find('w') == -1:
                                    if shoot > 0:
                                        dir = drawTurnLeft(dir)
                                        shoot -= 1
                                        print("\nremaining shoot is ", shoot, "\n")
                                        shoot_w(i, j, dir)
                                    else:
                                        alertShoot()
                                        print("\nremaining shoot is ", shoot, "\n")
                            else:
                                if shoot > 0:
                                    shoot -= 1
                                    print("\nremaining shoot is ", shoot, "\n")
                                    shoot_w(i, j, dir)
                                else:
                                    alertShoot()
                                    print("remaining shoot is ", shoot, "\n")
                        elif i == 3:
                            if user_grid[3-i-1][j].find('w') != -1: #내 오른쪽에 있어
                                if dead_wumpus[3-i-1][j].find('w') == -1:
                                    if shoot > 0:
                                        dir = drawTurnRight(dir)
                                        shoot -= 1
                                        print("\nremaining shoot is ", shoot, "\n")
                                        shoot_w(i, j, dir)
                                    else:
                                        alertShoot()
                                        print("\nremaining shoot is ", shoot, "\n")
                            else:
                                if shoot > 0:
                                    shoot -= 1
                                    print("\nremaining shoot is ", shoot, "\n")
                                    shoot_w(i, j, dir)
                                else:
                                    alertShoot()
                                    print("remaining shoot is ", shoot, "\n")

                        else:
                            if user_grid[3-i-1][j].find('w') != -1: #내 오른쪽에 있어
                                if dead_wumpus[3-i-1][j].find('w') == -1:
                                    if shoot > 0:
                                        dir = drawTurnRight(dir)
                                        shoot -= 1
                                        print("\nremaining shoot is ", shoot, "\n")
                                        shoot_w(i, j, dir)
                                    else:
                                        alertShoot()
                                        print("\nremaining shoot is ", shoot, "\n")
                            elif user_grid[3-i+1][j].find('w') != -1: #내 왼쪽에 웜퍼스 있음
                                if dead_wumpus[3-i][j-1].find('w') == -1:
                                    if shoot > 0:
                                        dir = drawTurnLeft(dir)
                                        shoot -= 1
                                        print("\nremaining shoot is ", shoot, "\n")
                                        shoot_w(i, j, dir)
                                    else:
                                        alertShoot()
                                        print("\nremaining shoot is ", shoot, "\n")
                            else:
                                if shoot > 0:
                                    shoot -= 1
                                    print("\nremaining shoot is ", shoot, "\n")
                                    shoot_w(i, j, dir)
                                else:
                                    alertShoot()
                                    print("remaining shoot is ", shoot, "\n")

                if user_grid[3 - i][j - 1].find('p') != -1:
                    if i == 0:
                        if user_grid[3-i-1][j].find('p') == -1:
                            dir = drawTurnRight(dir)
                    elif i == 3:
                        if user_grid[3-i+1][j].find('p') == -1:
                            dir = drawTurnLeft(dir)
                    else:
                        if user_grid[3-i-1][j].find('p') == -1 and user_grid[3-i+1][j].find('p') == -1:
                            dir = randomdir(dir)
                        elif user_grid[3-i-1][j].find('p') != -1 and user_grid[3-i+1][j].find('p') == -1:
                            dir = drawTurnLeft(dir)
                        elif user_grid[3-i-1][j].find('p') == -1 and user_grid[3-i+1][j].find('p') != -1:
                            dir = drawTurnRight(dir)
                else:
                    if percept_play_grid[3-i][j].find('b') != -1:
                        print("I can feel b in (", i, j, ")\n")
                        alertBreeze()
                        if i == 0:
                            if user_grid[3-i-1][j].find('p') == -1:
                                dir = drawTurnRight(dir)
                        elif i == 3:
                            if user_grid[3-i+1][j].find('p') == -1:
                                dir = drawTurnLeft(dir)
                        else:
                            if user_grid[3-i-1][j].find('p') == -1 and user_grid[3-i+1][j].find('p') == -1:
                                dir = randomdir(dir)
                            elif user_grid[3-i-1][j].find('p') != -1 and user_grid[3-i+1][j].find('p') == -1:
                                dir = drawTurnLeft(dir)
                            elif user_grid[3-i-1][j].find('p') == -1 and user_grid[3-i+1][j].find('p') != -1:
                                dir = drawTurnRight(dir)
            else: #현재 내 자리에
                if percept_play_grid[3 - i][j].find('b') != -1:
                    print("I can feel b in (", i, j, ")\n")
                    alertBreeze()
                    if i == 3:
                        if user_grid[3-i+1][j].find('p') == -1:
                            dir = drawTurnLeft(dir)
                        else:
                            dir = drawTurnLeft(dir)
                            dir = drawTurnLeft(dir)
                    else:
                        if user_grid[3-i-1][j].find('p') == -1 and user_grid[3-i+1][j].find('p') == -1:
                            dir = randomdir(dir)
                        elif user_grid[3-i-1][j].find('p') != -1 and user_grid[3-i+1][j].find('p') == -1:
                            dir = drawTurnLeft(dir)
                        elif user_grid[3-i-1][j].find('p') == -1 and user_grid[3-i+1][j].find('p') != -1:
                            dir = drawTurnRight(dir)
                        else:
                            dir = drawTurnRight(dir)
                            dir = drawTurnRight(dir)

        else:
            if not (i == 3): #현재 내 진행 방향에
                if user_grid[3 - i - 1][j].find('w') != -1: #웜퍼스가 있는걸 알아
                    if dead_wumpus[3-i-1][j].find('w') == -1: #근데 아직 안죽임
                        if shoot > 0:
                            shoot -= 1
                            print("\nremaining shoot is ", shoot, "\n")
                            alertScream()
                            delete_s(i, j, dir)
                        else:
                            alertShoot()
                            print("\nremaining shoot is ", shoot, "\n")
                else: #모르는데
                    if percept_play_grid[3 - i][j].find('s') != -1: #s가 느껴져
                        print("I can feel s in (", i, j, ")\n")
                        alertStench()
                        if j == 3:
                            if user_grid[3-i][j-1].find('w') != -1: #왼쪽에 있는걸 알아
                                if dead_wumpus[3-i][j-1].find('w') == -1: #근데 아직 안죽임
                                    if shoot > 0:
                                        dir = drawTurnLeft(dir)
                                        print("바뀐 방향: ",dir)
                                        shoot -= 1
                                        print("\nremaining shoot is ", shoot, "\n")
                                        shoot_w(i, j, dir)
                                    else:
                                        alertShoot()
                                        print("\nremaining shoot is ", shoot, "\n")
                            else:
                                if shoot > 0:
                                    shoot -= 1
                                    print("\nremaining shoot is ", shoot, "\n")
                                    shoot_w(i, j, dir)
                                else:
                                    alertShoot()
                                    print("\nremaining shoot is ", shoot, "\n")
                        elif j == 0:
                            if user_grid[3-i][j+1].find('w') != -1: #오른쪽에 있는걸 알아
                                if dead_wumpus[3-i][j+1].find('w') == -1:
                                    if shoot > 0:
                                        dir = drawTurnRight(dir)
                                        print("바뀐 방향: ", dir)
                                        shoot -= 1
                                        print("\nremaining shoot is ", shoot, "\n")
                                        shoot_w(i, j, dir)
                                    else:
                                        alertShoot()
                                        print("\nremaining shoot is ", shoot, "\n")
                            else:
                                if shoot > 0:
                                    shoot -= 1
                                    print("\nremaining shoot is ", shoot, "\n")
                                    shoot_w(i, j, dir)
                                else:
                                    alertShoot()
                                    print("\nremaining shoot is ", shoot, "\n")
                        else:
                            if user_grid[3-i][j+1].find('w') != -1:
                                if dead_wumpus[3-i][j+1].find('w') == -1:
                                    if shoot > 0:
                                        dir = drawTurnRight(dir)
                                        print("바뀐 방향: ", dir)
                                        shoot -= 1
                                        print("\nremaining shoot is ", shoot, "\n")
                                        shoot_w(i, j, dir)
                                    else:
                                        alertShoot()
                                        print("\nremaining shoot is ", shoot, "\n")
                            elif user_grid[3-i][j-1].find('w') != -1:
                                if dead_wumpus[3-i][j-1].find('w') == -1:
                                    if shoot > 0:
                                        dir = drawTurnLeft(dir)
                                        print("바뀐 방향: ", dir)
                                        shoot -= 1
                                        print("\nremaining shoot is ", shoot, "\n")
                                        shoot_w(i, j, dir)
                                    else:
                                        alertShoot()
                                        print("\nremaining shoot is ", shoot, "\n")
                            else:
                                if shoot > 0:
                                    shoot -= 1
                                    print("\nremaining shoot is ", shoot, "\n")
                                    shoot_w(i, j, dir)
                                else:
                                    alertShoot()
                                    print("\nremaining shoot is ", shoot, "\n")


                if user_grid[3-i-1][j].find('p') != -1:
                    if j == 0:
                        if user_grid[3-i][j+1].find('p') == -1:
                            dir = drawTurnRight(dir)
                    elif j == 3:
                        if user_grid[3-i][j-1].find('p') == -1:
                            dir = drawTurnLeft(dir)
                    else:
                        if user_grid[3-i][j-1].find('p') == -1 and user_grid[3-i][j+1].find('p') == -1:
                            if i == 0 and j == 1:
                                dir = drawTurnRight(dir)
                            else:
                                dir = randomdir(dir)
                        elif user_grid[3-i][j-1].find('p') != -1 and user_grid[3-i][j+1].find('p') == -1:
                            dir = drawTurnRight(dir)
                        elif user_grid[3-i][j-1].find('p') == -1 and user_grid[3-i][j+1].find('p') != -1:
                            dir = drawTurnLeft(dir)
                else:
                    if percept_play_grid[3-i][j].find('b') != -1:
                        print("I can feel b in (", i, j, ")\n")
                        alertBreeze()
                        if j == 0:
                            if user_grid[3-i][j+1].find('p') == -1:
                                dir = drawTurnRight(dir)
                        elif j == 3:
                            if user_grid[3-i][j-1].find('p') == -1:
                                dir = drawTurnLeft(dir)
                        else:
                            if user_grid[3-i][j-1].find('p') == -1 and user_grid[3-i][j+1].find('p') == -1:
                                dir = randomdir(dir)
                            elif user_grid[3-i][j-1].find('p') != -1 and user_grid[3-i][j+1].find('p') == -1:
                                dir = drawTurnRight(dir)
                            elif user_grid[3-i][j-1].find('p') == -1 and user_grid[3-i][j+1].find('p') != -1:
                                dir = drawTurnLeft(dir)



            else:
                if percept_play_grid[3 - i][j].find('b') != -1:
                    print("I can feel b in (", i, j, ")\n")
                    alertBreeze()
                    if j == 0:
                        if user_grid[3-i][j+1].find('p') == -1:
                            dir = drawTurnRight(dir)
                        else:
                            dir = drawTurnLeft(dir)
                            dir = drawTurnLeft(dir)
                    elif j == 3:
                        if user_grid[3-i][j-1].find('p') == -1:
                            dir = drawTurnLeft(dir)
                        else:
                            dir = drawTurnRight(dir)
                            dir = drawTurnRight(dir)
                    else:
                        if user_grid[3-i][j-1].find('p') == -1 and user_grid[3-i][j+1].find('p') == -1:
                            dir = randomdir(dir)
                        elif user_grid[3-i][j-1].find('p') != -1 and user_grid[3-i][j+1].find('p') == -1:
                            dir = drawTurnRight(dir)
                        elif user_grid[3-i][j-1].find('p') == -1 and user_grid[3-i][j+1].find('p') != -1:
                            dir = drawTurnLeft(dir)
                        else:
                            dir = drawTurnRight(dir)
                            dir = drawTurnRight(dir)
        print("\n현재 grid")
        for q in range(4):
            print(play_grid[q])
        print("\n현재 percept")
        for q in range(4):
            print(percept_play_grid[q])
        print("\n")







    if gold == 1:
        break

        print("\n\n 결과값")
        print("percept_grid")
        for h in range(4):
            print(percept_grid[h])
        print("\n")
        print("play_grid")
        for h in range(4):
            print(play_grid[h])
        print("\n visited_grid")
        for h in range(6):
            print(visited_grid[h])
        print("\n user_grid")
        for h in range(4):
            print(user_grid[h])
