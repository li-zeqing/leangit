#张三爬一段15阶的楼梯
#张三一步最多上3个台阶
#分别用递归法和递推法计算一共用几种方法上15阶楼梯

#递归法
def climb_stairs_back(n):
    #定义一个字典
    # 当处在第1台阶时有1种方法上
    # 当处在第2台阶时有2种方法上
    # 当处在第3台阶时有4种方法上
    A = {1:1,2:2,3:4}
    if n in A.keys():
        return A[n]
    else:
        return climb_stairs_back(n-1)+climb_stairs_back(n-2)+climb_stairs_back(n-3)

#递推法
def climb_stairs_push(n):

    a = 1
    b = 2
    c = 4
    for i in range(n-3):
        c,b,a = a+b+c,c,b
    return c
#递推法2
def climb_stairs_push_2(n):
    f = [0]*50
    f[1] = 1
    f[2] = 2
    f[3] = 4
    for i in range(4,50,1):
        f[i] = f[i-1] +f[i-2]+f[i-3]
    return f[n]
if __name__ == '__main__':
    print("递归法求上15级台阶的走法：",climb_stairs_back(15))
    print("递推法1求上15级台阶的走法：",climb_stairs_push(15))
    print("递推法2求上15级台阶的走法：",climb_stairs_push_2(15))





