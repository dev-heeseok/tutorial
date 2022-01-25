import turtle as t 

# 1. 정사각형 그리기
for i in range(4):
    t.forward(100) # t.fd(100)
    t.left(90)
    print(t.pos())

# 2. 평행사변형 그리기
t.up() # draw unset
t.goto(200, 0)
t.down() # draw set

for i in range(2):
    t.fd(120)
    t.left(120)
    t.fd(80)
    t.left(60)
    print(t.pos())

# 3. 별 모양 그리기
t.up()
t.goto(-200, 0)
t.down()

for i in range(5):
    t.fd(100)
    t.right(360*2 // 5)

# 4. 기하학적인 도형 그리기
t.up()
t.goto(0, 300)
t.down()

t.color('red', 'yellow')
t.begin_fill() # 채우기 시작 

while(True):
    t.forward(100)
    t.left(170)
    x, y = t.pos()
    if int(x) == 0 and int(y) == 300:
        print(t.pos())
        print(abs(t.pos()))
        break

t.end_fill() # 채우기 종료
t.done() 

