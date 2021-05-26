#绘制n阶谢尔宾斯基三角形
#递归方法：基例，0阶，1阶谢尔宾斯基三角形
import turtle as t
import math
# 根据三个坐标点画三角形
def draw_triangle(point1, point2, point3,n):
    t.penup()
    t.goto(point1)
    t.pendown()
    t.goto(point2)
    t.goto(point3)
    t.goto(point1)
    n = n-1
# 根据两个坐标点,返回中点坐标(元组)
def getmid(point_a, point_b):
    return (point_a[0] + point_b[0]) * 0.5, (point_a[1] + point_b[1]) * 0.5

def sierpinski(point1, point2, point3,n):
    # 调用画三角形函数
    draw_triangle(point1, point2, point3,n)
    # n为递归次数,每递进一层n-1,当n=0停止
    if n:
        # 递进一层,每通过一个顶点和另外两个中点得到一个小三角形,每层递进三次
        sierpinski(point1, getmid(point1, point2), getmid(point1, point3),n-1)
        sierpinski(point2, getmid(point2, point1), getmid(point2, point3),n-1)
        sierpinski(point3, getmid(point3, point1), getmid(point3, point2),n-1)

if __name__ == '__main__':
    t.setup(800,800)
    t.pensize(5)
    t.speed(5)
    t.hideturtle()
    # 提供三个点的坐标,与形状无关,只要能组成三角形即可
    point1, point2, point3 = [-250, -200], [250, -200], [0, 200]
    #绘制n阶
    n = 3
    # 主函数调用
    sierpinski(point1, point2, point3, n)
    t.done()
