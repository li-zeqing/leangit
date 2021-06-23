#中国居民身份证示例：432831 19641115 0810
# 中国目前采用的是18位身份证号，其第7-10位数字是出生年，11-12位是出生月份，13-14是出生日期，
# 第17位是性别，奇数为男性，偶数为女性，第18位是校验位。
# 如果身份证号码的其中一位填错了（包括最后一个校验位），则校验算法可以检测出来。
# 如果身份证号的相邻2位填反了，则校验算法可以检测出来。校验规则如下：
# 1. 将前面的身份证号码17位数分别乘以不同的系数。
#   从第一位到第十七位的系数分别为：7－9－10－5－8－4－2－1－6－3－7－9－10－5－8－4－2。
# 2. 将这17位数字和系数相乘的结果相加。
# 3. 用加出来和除以11，看余数只可能是：0－1－2－3－4－5－6－7－8－9－10
#     分别对应的最后一位身份证的号码为：1－0－X－9－8－7－6－5－4－3－2
# 4. 通过上面得知如果余数是2，就会在身份证的第18位数字上出现罗马数字的X（大写英文字母X）。
#    如果余数是10，身份证的最后一位号码就是2。
#
# 用户输入一个身份证号，校验其是否是合法的身份证号码:
# 1. 输入长度是否合法
# 2. 输入数据校验位是否合法
# 3. 输入数据中年月日范围是否合法，考虑闰年。
# 如身份证号码不合法输出 '身份证校验错误'，
# 如身份证号码合法则分别在4行中输出'身份证号码校验为合法号码!'以及该人的出生年月日、年龄和性别。
import datetime  # 导入datetime模块用于获取当年年份


def leap(year_born):
    return True if (year_born % 400 == 0) or (year_born % 4 == 0 and year_born % 100 != 0) else False


# 校验身证号中的年月日及校验码
def id_check(id_number):
    # 年份超过当前年，或月份小于1或大于12，或日期小于1或大于31时非法
    if int(id_number[6:10]) > datetime.datetime.now().year or int(id_number[10:12]) < 1 or int(
            id_number[10:12]) > 12 or int(
            id_number[12:14]) < 1 or int(id_number[12:14]) > 31:
        return False
    # 当月份为4，6，9，11时，日期超过30即非法
    if int(id_number[10:12]) in [4, 6, 9, 11] and int(id_number[12:14]) > 30:
        return False
    # 月份为2时，日期大于29便非法
    if int(id_number[10:12]) == 2 and int(id_number[12:14]) > 29:
        return False
    # 月份为2时，如果不是闰年，日期大于28便非法
    if int(id_number[10:12]) == 2 and not leap(year) and int(id_number[12:14]) > 28:
        print(year)
        return False
    # 计算校验和
    ls = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1]
    total = sum([ls[i] * int(id_number[i]) for i in range(17)])
    if id_number[17] == 'X':
        return True if total % 11 == 2 else False
    elif (total % 11 + int(id_number[17])) % 11 == 1:
        return True
    else:
        return False


id_num = input()
year = int(id_num[6:10])
month = id_num[10:12]
day = id_num[12:14]
if len(id_num) == 18 and id_check(id_num):  # 先判断长度是否是18位，再判断校验和
    gender = '女' if int(id_num[16]) % 2 == 0 else '男'
    print('身份证号码校验为合法号码')
    print('出生：{}年{}月{}日'.format(year, month, day))
    print('年龄：{}'.format(datetime.datetime.now().year - year))
    print('性别：{}'.format(gender))
else:
    print('身份证校验错误')