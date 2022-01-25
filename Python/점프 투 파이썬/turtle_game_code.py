import time
from turtle import *
from random import randint

speed(30)
up()
goto(-140, 140)

for i in range(16):
    write(i, align='center') # text 
    right(90)
    fd(10)
    down()
    fd(150)
    up()
    bk(160)
    left(90)
    fd(20)

finish_line = xcor() - 20
print('finish line :', finish_line)

tutle_color = ['red', 'blue', 'green', 'gold']
tutle_list = []

for i in range(len(tutle_color)):
    t = Turtle() # 거북이 선수 생성
    t.color(tutle_color[i]) # 거북이 선수 색상
    t.shape('turtle') # 거북이 모양
    t.up() # 팬을 업
    t.goto(-160, 140 - 30 * (i + 1))
    t.down()
    tutle_list.append(t)

def start_game():
    while(True):
        for t in tutle_list:
            dist = randint(5, 10)
            t.fd(dist)
            if t.xcor() >= finish_line:
                return t

my_game = start_game()

for i in range(1, 10):
    my_game.shapesize(i, i)
    time.sleep(0.1)

for i in range(18 * 3):
    my_game.right(20)

goto(0, 0)
color_name = str(my_game.color()[0])
write('Congratulation ' + color_name, align='center', font=('Arial', 20, 'normal'))

