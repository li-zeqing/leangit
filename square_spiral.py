#绘制正方形螺旋
import turtle as t
t.setup(1200,800)
#画笔粗细
t.pensize(3)
#画笔颜色
t.pencolor("blue")
t.speed(10)
t.penup()
t.goto(-300,-200)
t.pendown()
t.seth(90)
x_length = 500
s_length = 7
for i in range((int)(x_length/s_length)):
    for i in range(2):
        x_length = x_length - s_length
        for i in range(2):
            t.fd(x_length)
            t.right(90)
    if x_length<=35 :
        t.pencolor("red")
    t.speed(10**(i+1))
t.done()
