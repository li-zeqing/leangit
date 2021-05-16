# 尼姆游戏(人机对战)
# 两个玩家轮流从一堆物品中拿走一部分,在每一步中,玩家可以自由选择拿走多少物品,但必须至少拿走一个且最多只能拿走一半物品,
# 然后轮到下一个玩家。拿走最后一个物品,的玩家输掉游戏。
# 在聪明模式中，计算机玩家每次拿走一定数量的物品使得剩下的数量是2的幂次方减1-即3、7、15、31、63等。
# 如果无法做到这一点,计算机则随机拿走一些。
# 编写程序，模拟聪明版本的尼姆游戏。
import math
import random

#2的幂次方减1
#math.pow(2,y) = 100 则y = math.log2(100)
#计算机每次拿走C_take,玩家拿走P_take

#定义一个取物品函数，参数a判断此时是C_take还是P_take拿走物品，返回剩余物品数目num_residue
def takegoods(a=["P_take","C_take"], num_residue=None):
    if a =="P_take":
        P_take = int(input("请输入次数你需要拿的物品数量(输入数字需<=剩余物品的一半): "))
        if(num_residue!=1):
            if P_take > num_residue/2:
                print("拿走的物品多于一半，请重新输入拿走物品数目!!!!!!")
                P_take = int(input("请输入次数你需要拿的物品数量(输入数字需<=剩余物品的一半): "))
        print("玩家拿走：", P_take)
        return num_residue - P_take
    else:
        if num_residue - (math.pow(2, int(math.log2(num_residue))) - 1) <= num_residue/2:
            # 计算机玩家每次拿走一定数量的物品使得剩下的数量是2的幂次方减1 - 即3、7、15、31、63等
            C_take = num_residue - (math.pow(2, int(math.log2(num_residue))) - 1)
        else:
            #不能满足以上条件就随机拿取，当剩余物品为1时，只能拿1
            C_take = random.randint(1,int(num_residue/2)) if num_residue>1 else 1
        print("计算机拿走：", C_take)
        return num_residue - C_take
#定义一个取物品游戏的函数，输入一堆物品的数目，当最后拿物品的是玩家就返回1，如果最后拿物品的是计算机就返回2
def takegoos_play():
    # 一堆物品
    # num = 100
    try:
        num = int(input("请输入这一堆物品的数目(需为int型正整数): "))
        # 剩余物品
        num_residue = num
        print("一堆物品：", num_residue)
        while (num_residue != 0):
            # 规定玩家先开始拿物品
            num_residue = takegoods("P_take",num_residue)
            print("剩余物品：", num_residue)
            if (num_residue == 0):
                return 1  # 记录最后拿物品的是谁，玩家拿的为1

            num_residue = takegoods("C_take",num_residue)
            print("剩余物品：", num_residue)
            print('*' * 20)
            if (num_residue == 0):
                return 2  ##记录最后拿物品的是谁，计算机拿的为0
    except:
        print("你输入的数字有误！")

if __name__ == '__main__':
    print('-'*50,"欢迎来到尼玛游戏",'-'*50)
    #最后拿走物品
    is_end = takegoos_play()
    if(is_end ==1):
        print("最后拿物品的是玩家！")
        print("计算机获胜")
    else:
        print("最后拿物品的是计算机！")
        print("玩家获胜")
    print('-' * 50, "游戏结束", '-' * 50)
    print('-' * 49, "想变强 请充值", '-' * 48)
