#选择一文本进度条函数进行改进文本进度 f(x) = 1+(1-x)^3*-1
import time
import math
scale = 100
print("执行开始".center(scale//2,'-'))
t = time.perf_counter()
for i in range(scale+1):
    #函数f(x) = 1+(1-x)^3*-1
    y = 1 - pow((1.0 - i*0.01),3)
    i = math.floor(y*100)   #向下取整
    a = '*'*i
    b = ' '*(scale-i)
    c = (i/scale)*100
    t -= time.perf_counter()
    print("\rStart[{1}->{2}]{0:>3.0f}% {3:.2f}s".format(c,a,b,-t),end='')
    time.sleep(0.5)
print("\n"+"执行结束".center(scale//2,'-'))