#身高预测：用户从键盘输入用户性别（F，M）、父亲身高（单位为cm）、
# 母亲身高、是否喜爱体育锻炼（Y、N）、是否有良好的饮食习惯
#身高计算公式：男性=(hf+hm)*0.54cm 女性=(hf*0.923+hm)/2cm
#如果喜欢体育锻炼可增加身高2%,如果有良好的饮食习惯，可增加身高1.5%
import math
str = input("请输入你的信息：")
#输入示例：F,175cm,175cm,Y,N  输出为：172cm
list_str = str.split(',')
hf = int(list_str[1][:-2])
hm = int(list_str[2][:-2])
if(list_str[0]=='M'):
    Hight  = float((hf + hm)*0.54)
else:
    Hight = float(math.fsum([hf*0.923,hm])*0.5)
if(list_str[3]=='Y'):
    Hight = Hight*math.fsum([1.0,0.02])
if(list_str[4]=='Y'):
    Hight = Hight*math.fsum([1.0,0.015])
print("你的预测身高为："+Hight.__round__().__str__()+"{}".format("cm"))