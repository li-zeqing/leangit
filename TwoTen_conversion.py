#十进制转二进制
c = []
a = input("请输入十进制或者二进制数字：")
# 定义一个函数 二进制整数转十进制
def Two_to_Ten_integer(a):
    if (a[:2] == '0b') | (a[:2] == '0B'):
        a = list(map(int, a[2:]))   #map返回一个集合
        d = len(a)
        ff_integer = 0
        for i in a:
            d = d - 1
            ff_integer = ff_integer + i * (2 ** d)
        return int(ff_integer)

    else:
        a = list(map(int, a[3:]))
        d = len(a)
        ff_integer = 0
        for i in a:
            d = d - 1
            ff_integer = ff_integer + i * (2 ** d)
        ff_integer = -ff_integer
        return int(ff_integer)

#定义一个函数 二进制小数部分转十进制
def Two_to_Ten_decimal(a_decimal):
    a_decimal = list(map(int, a_decimal))
    ff = 0
    j = 1
    for i in a_decimal:
        ff = ff + i*2**(-j)
        j = j +1
    return ff

#定义一个函数 十进制转二进制
def Ten_to_Two_integer(a):
    while True:
        div = a // 2
        # print(div)
        mod = a % 2
        # print(mod)
        c.append(mod)
        a = div
        # print(div)
        if a == 0:
            break
        else:
            continue
    c.reverse()  # 逆序
    # print("&&&&&",c)
    D = list(map(str, c))  # 将c以字符型数据存储在list中
    return D

#定义一个函数 十进制小数部分转二进制
def Ten_to_Two_decimal(a):
    x = []
    s = []
    while (a):
        a = a * 2
        x.append(str(int(a)))
        a = a - int(a)
    if len(x)>=10:
        for i in range(0, 10):
            s.append(x[i])
    else:
        for i in range(0, len(x)):
            s.append(x[i])
    return "".join(s)

#定义一个函数 十进制整体转化二进制
def Ten_to_Two_all(a_integer, a_decimal_f):
    a_integer = int(a_integer)
    D1 = Ten_to_Two_integer(a_integer)
    D1 = "".join(D1)  # 以字符串输出整数部分的二进制
    a_decimal_f = Ten_to_Two_decimal(a_decimal_f)  # 以字符串输出小数部分的二进制
    # 连接整数和小数部分输出
    return '.'.join([D1, a_decimal_f])

#输入为二进制时
if (a[:2] == '0b')|(a[:2] == '0B')|(a[:3] == '-0b')|(a[:3] == '-0B'):
    if a.count('.') == 0 :
        #二进制整数转十进制
        ff_integer = Two_to_Ten_integer(a)
        print("十进制：",ff_integer)
    else:
        # 以小数点分隔字符串
        a_integer = a.split('.')[0]
        a_decimal = a.split('.')[1]
        # 二进制整数转十进制
        ff_integer = Two_to_Ten_integer(a_integer)
        # 二进制小数部分转十进制
        Two_to_Ten_decimal(a_decimal)
        if(ff_integer>0):
            print("十进制：",ff_integer+Two_to_Ten_decimal(a_decimal))
        else:
            print("十进制：", ff_integer - Two_to_Ten_decimal(a_decimal))
#输入为十进制时
else:
    if a.count('.') == 0:
        a = int(a)
        #判断十进制的正负 再转换为二进制
        if a>=0:
            D = Ten_to_Two_integer(a)
            print("二进制：",''.join(D)+".0")   #字符拼接为一个字符串
        else:
            a = -a  #负数取反
            D = Ten_to_Two_integer(a)
            print("二进制：","-"+''.join(D)+".0")  # 字符拼接为一个字符串
    else:
        # 以小数点分隔字符串
        a_integer = a.split('.')[0]
        a_decimal = a.split('.')[1]
        a_decimal_f = float((int(a_decimal)) * 10 ** (-len(a_decimal)))
        # print(a_decimal_f)
        # print(type(a_decimal_f))
        #十进制整数部分转二进制
        if a[0] != '-':
            # Ten_to_Two_all(a_integer, a_decimal_f)
            #连接整数和小数部分输出
            print("二进制：",Ten_to_Two_all(a_integer, a_decimal_f))
        else:
            a_integer = a_integer[1:]
            # Ten_to_Two_all(a_integer, a_decimal_f)
            print("二进制：",'-'+Ten_to_Two_all(a_integer, a_decimal_f))


