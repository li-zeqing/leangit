# 温度转换异常处理
# 转换算法如下：（C表示摄氏度、F表示华氏度）
# C = ( F - 32 ) / 1.8
# F = C * 1.8 + 32
# 要求如下：
# (1) 输入输出的摄氏度采用大写字母 C 或小写字母 c 结尾，温度可以是整数或小数，如：12.34C 指摄氏度 12.34 度；
# (2) 输入输出的华氏度采用大写字母 F 或小字字母 f 结尾，温度可以是整数或小数，如：87.65F 指华氏度 87.65 度
# (3) 考虑异常输入的问题，如输入不合法则抛出异常；
# (4) 使用input()获得测试用例输入时，不要增加提示字符串。
try:
    T = input()
    if T[-1] in ['C','c']:
        F = eval(T[:-1])*1.8 + 32
        print("{:.2f}F".format(F))
    elif T[-1] in ['F','f']:
        C = (eval(T[:-1]) - 32)/1.8
        print("{:.2f}C".format(C))
    else:
        print("输入错误，末位只能是'C','c','F','f'")
except NameError:
    print("试图访问的变量名不存在")
except SyntaxError:
    print("存在语法错误")
except Exception as e:
    print(e)