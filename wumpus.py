import time
import tkinter
import tkinter.ttk
from tkinter import *
import turtle
import random

# shoot 횟수
shoot_num = 3
# agent 방향
current_orient = "East"
# x좌표, y좌표
x = -210
y = -200

# turtle 배경
def drawTurtle():
    scr = turtle.Screen()
    scr.setup(590, 650)
    scr.bgpic("turtle.gif")
    scr.update()

    # turtle title
    turtle.penup()
    turtle.sety(280)
    turtle.pendown()
    turtle.write("Wumpus World", move = False, align = "center", font = ("Arial", 15, "normal"))

    # turtle 초기 위치 (x = -210, y = -200)
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()

# Percepts
# Stench 알림
def alertStench ():
    turtle.penup()
    turtle.setx(0)
    turtle.sety(-290)
    turtle.write("Percept = Stench", move = False, align = "center", font = ("Arial", 12, "normal"))
    time.sleep(1)
    turtle.undo()

# Breeze 알림
def alertBreeze ():
    turtle.penup()
    turtle.setx(0)
    turtle.sety(-290)
    turtle.write("Percept = Breeze", move = False, align = "center", font = ("Arial", 12, "normal"))
    time.sleep(1)
    turtle.undo()

# Glitter 알림
def alertGlitter ():
    turtle.penup()
    turtle.setx(0)
    turtle.sety(-290)
    turtle.write("Percept = Glitter", move = False, align = "center", font = ("Arial", 12, "normal"))
    time.sleep(1)
    turtle.undo()

# Bump 알림
def alertBump ():
    turtle.penup()
    turtle.setx(0)
    turtle.sety(-290)
    turtle.pendown()
    turtle.write("Percept = Bump", move = False, align = "center", font = ("Arial", 12, "normal"))
    time.sleep(1)
    turtle.undo()

# Scream 알림 (shoot 성공 시)
def alertScream ():
    turtle.penup()
    turtle.setx(0)
    turtle.sety(-290)
    turtle.pendown()
    # Shoot
    turtle.write("Action = Shoot", move = False, align = "center", font = ("Arial", 12, "normal"))
    time.sleep(1)
    turtle.undo()
    turtle.write("Percept = Scream", move = False, align = "center", font = ("Arial", 12, "normal"))
    time.sleep(1)
    turtle.undo()
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()

# pit에서 죽은 경우
def alertPitDie ():
    turtle.penup()
    turtle.setx(0)
    turtle.sety(-290)
    turtle.write("There is a Pit !", move = False, align = "center", font = ("Arial", 12, "normal"))
    time.sleep(1)
    turtle.undo()
    turtle.write("You die", move=False, align="center", font=("Arial", 12, "normal"))
    time.sleep(1)
    turtle.undo()

# wumpus에서 죽은 경우
def alertWumpusDie ():
    turtle.penup()
    turtle.setx(0)
    turtle.sety(-290)
    turtle.write("There is a Wumpus !", move = False, align = "center", font = ("Arial", 12, "normal"))
    time.sleep(1)
    turtle.undo()
    turtle.write("You die", move=False, align="center", font=("Arial", 12, "normal"))
    time.sleep(1)
    turtle.undo()

# Action
# Go forward
def drawGoForward (i,j, dir):
    # 속도 느리게
    turtle.speed(3)

    global x
    global y

    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()

    if not ((i == 0 and j==3 and (dir == 0 or dir ==1)) or (i == 0 and dir == 1) or (i == 3 and dir == 3) or (j == 0 and dir == 2) or (j == 3 and dir == 0) or (i == 3 and j==3 and (dir == 0 or dir ==3)) or (i == 3 and j==0 and (dir == 2 or dir ==3)) ):
        turtle.forward(140)

        if dir == 0:
            x += 140
        elif dir == 1:
            y -= 140
        elif dir == 2:
            x -= 140
        elif dir == 3:
            y += 140

    if dir == 0:
        j += 1
    elif dir == 3:
        i += 1
    elif dir == 2:
        j -= 1
    elif dir == 1:
        i -= 1

    return i, j, x, y

# drawBackward
# -200, -60, 80, 220
# -210, -70, 70, 210
def set_x (i, visited_x):
    if visited_x[i] == 0:
        turtle.sety(-200)
    if visited_x[i] == 1:
        turtle.sety(-60)
    if visited_x[i] == 2:
        turtle.sety(80)
    if visited_x[i] == 3:
        turtle.sety(220)

def set_y (i, visited_y):
    if visited_y[i] == 0:
        turtle.setx(-210)
    if visited_y[i] == 1:
        turtle.setx(-70)
    if visited_y[i] == 2:
        turtle.setx(70)
    if visited_y[i] == 3:
        turtle.setx(210)

def drawBackward (visit_len, visited_x, visited_y):
    # 속도 느리게
    turtle.speed(3)
    s = visit_len
    visited_x.reverse()
    visited_y.reverse()
    visited_x.append(0)
    visited_y.append(0)

    for i in range(s):
        if i == 0: # 초기 상태
            turtle.penup()
        set_x(i, visited_x)
        set_y(i, visited_y)
        if i == 0: # 초기 상태
            turtle.pendown()

    turtle.goto(-210, -200)


# Turn left
def drawTurnLeft (dir):
    turtle.left(90)

    # 방향 바꿔주기
    dir -= 1
    if dir < 0:
        dir = 3
    return dir

# Turn right
def drawTurnRight (dir):
    turtle.right(90)

    # 방향 바꿔주기
    dir += 1
    if dir > 3:
        dir = 0
    return dir

# Shoot 알림
def alertShoot ():
    turtle.penup()
    turtle.setx(0)
    turtle.sety(-290)
    turtle.pendown()
    # Shoot
    turtle.write("Action = Shoot", move = False, align = "center", font = ("Arial", 12, "normal"))
    time.sleep(1)
    turtle.undo()
    # shoot 실패했을 때
    turtle.write("Fail to shoot", move = False, align = "center", font = ("Arial", 12, "normal"))
    time.sleep(1)
    turtle.undo()

# Grab 성공 알림
def alertSuccessGrab ():
    turtle.penup()
    turtle.setx(0)
    turtle.sety(-290)
    # Grab
    turtle.write("Action = Grab", move=False, align="center", font=("Arial", 12, "normal"))
    time.sleep(1)
    turtle.undo()

    # grab 성공했을 때
    turtle.write("Action = Climb", move = False, align = "center", font = ("Arial", 12, "normal"))
    time.sleep(1)
    turtle.undo()

# Grab 실패 알림
def alertFailGrab ():
    turtle.penup()
    turtle.setx(0)
    turtle.sety(-290)
    # Grab
    turtle.write("Action = Grab", move=False, align="center", font=("Arial", 12, "normal"))
    time.sleep(1)
    turtle.undo()

    # grab 실패했을 때
    turtle.write("Fail to grab", move = False, align = "center", font = ("Arial", 12, "normal"))
    time.sleep(1)
    turtle.undo()

# Climb 알림
def alertClimb ():
    turtle.penup()
    turtle.setx(0)
    turtle.sety(-290)
    # Climb
    turtle.write("Climb", move=False, align="center", font=("Arial", 12, "normal"))
    time.sleep(1)
    turtle.undo()
    # 알고있는 경로로 돌아오기

# Wumpus table 그리기
def drawWumpusTable (wumpus_grid):
    root = tkinter.Tk()
    root.title("Wumpus World")
    root.geometry("500x200+100+100")
    root.resizable(False, False)
    lbl = tkinter.Label(root, text = "Current State")
    lbl.pack(pady = 10)

    # 표 생성
    treeview=tkinter.ttk.Treeview(root, columns = ["1", "2", "3", "4"], displaycolumns = ["1", "2", "3", "4"], height = 4)
    treeview.pack()

    # 컬럼 설정
    treeview.column("#0", width = 50,)
    treeview.heading("#0", text = "Index")

    treeview.column("#1", width = 50, anchor = "center")
    treeview.heading("1", text = "1", anchor = "center")

    treeview.column("#2", width = 50, anchor = "center")
    treeview.heading("2", text = "2", anchor = "center")

    treeview.column("#3", width = 50, anchor = "center")
    treeview.heading("3", text = "3", anchor = "center")

    treeview.column("#4", width = 50, anchor = "center")
    treeview.heading("4", text = "4", anchor = "center")

    # 표에 삽입될 데이터
    # treelist=[("", "", "", ""), ("", "Gold", "Pit", ""), ("", "", "Wumpus", ""), ("", "", "", "")]
    treelist = list(wumpus_grid)

    # 표에 데이터 삽입
    for i in range(len(treelist)):
        treeview.insert('', 'end', text = 4-i, values = treelist[i], iid = str(i)+"번")

    # 남은 shoot의 횟수, agent의 방향
    label1 = Label(root, text = "Shoot : ")
    label1.place(x = 150, y = 160)

    label2 = Label(root, text = shoot_num)
    label2.place(x = 200, y = 160)

    label3 = Label(root, text="Orientation : ")
    label3.place(x = 230, y = 160)

    label4 = Label(root, text=current_orient)
    label4.place(x = 310, y = 160)

    # GUI 실행
    root.mainloop()

def randomdir(dir):
    a = random.randint(0,1)
    b = dir
    if a == 0:
        c = drawTurnLeft(b)
    else:
        c = drawTurnRight(b)
    return c

def clearTurtle ():
    turtle.clear()
    global x
    global y

    turtle.penup()
    turtle.setx(0)
    turtle.sety(280)
    turtle.pendown()
    turtle.write("Wumpus World", move=False, align="center", font=("Arial", 15, "normal"))
    x = -210
    y = -200
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()
    turtle.setheading(0)

# User table 그리기
def drawUserTable (user_grid, shoot):
    root = tkinter.Tk()
    root.title("Wumpus World")
    root.geometry("500x200+100+100")
    root.resizable(False, False)
    lbl = tkinter.Label(root, text = "User Grid")
    lbl.pack(pady = 10)

    # 표 생성
    treeview=tkinter.ttk.Treeview(root, columns = ["1", "2", "3", "4"], displaycolumns = ["1", "2", "3", "4"], height = 4)
    treeview.pack()

    # 컬럼 설정
    treeview.column("#0", width = 50,)
    treeview.heading("#0", text = "Index")

    treeview.column("#1", width = 50, anchor = "center")
    treeview.heading("1", text = "1", anchor = "center")

    treeview.column("#2", width = 50, anchor = "center")
    treeview.heading("2", text = "2", anchor = "center")

    treeview.column("#3", width = 50, anchor = "center")
    treeview.heading("3", text = "3", anchor = "center")

    treeview.column("#4", width = 50, anchor = "center")
    treeview.heading("4", text = "4", anchor = "center")

    # 표에 삽입될 데이터
    # treelist=[("", "", "", ""), ("", "Gold", "Pit", ""), ("", "", "Wumpus", ""), ("", "", "", "")]
    treelist = list(user_grid)

    # 표에 데이터 삽입
    for i in range(len(treelist)):
        treeview.insert('', 'end', text = 4-i, values = treelist[i], iid = str(i)+"번")

    # 남은 shoot의 횟수, agent의 방향
    label1 = Label(root, text = "Shoot : ")
    label1.place(x = 210, y = 160)

    label2 = Label(root, text = shoot)
    label2.place(x = 260, y = 160)

    # GUI 실행
    root.mainloop()