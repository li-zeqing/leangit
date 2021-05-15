#猜数游戏：
#   先由计算机生成一个[m,n]的随机整数，如何人不断输入整数进行比较，并提示猜大了还是猜小了，
#   直到猜对或者猜的次数达到1.5*log2(n-m+1)次就结束游戏
import random
import math
def Guessing():
    try:
        m=int(input("请输入猜数游戏数字范围的下限m:"))
        n=int(input("请输入猜数游戏数字范围的上限n:"))
        random.seed(12)
        C_num = random.randint(m,n)
        P_num =m-1
        #记录人猜数的次数
        P_count = 0
        Max_count =int(1.5*math.log2(n-m+1))
        while(C_num!=P_num):
            try:
                P_num = int(input("请输入你猜想的整数："))
                P_count += 1
                if(P_num<C_num):
                    print("你猜小了")
                elif(P_num>C_num):
                    print("你猜大了")
                else:
                    print("恭喜你猜对了，你一共猜了{}次".format(P_count))
                if(P_count>=Max_count):
                    if(C_num !=P_num):
                        print("猜数次数过多，游戏结束。正确答案为:{}".format(C_num))
                    break
            except:
                print("你输入的为非整数，请输入int型数据")
    except:
        print("你输入的为非整数，请输入int型数据")
if __name__ == '__main__':
    print('-' * 50, "欢迎来到猜数游戏", '-' * 50)
    Guessing()
    print('-' * 50, "游戏结束", '-' * 50)
    print('-' * 49, "想变强 请充值", '-' * 48)
