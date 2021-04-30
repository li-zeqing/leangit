# 判定输入是否为数字，如果是，请输出该数字，否则，输出"这不是一个数字"
import unicodedata

CN_NUM = {
    '〇': 0,
    '一': 1,
    '二': 2,
    '三': 3,
    '四': 4,
    '五': 5,
    '六': 6,
    '七': 7,
    '八': 8,
    '九': 9,

    '零': 0,
    '壹': 1,
    '贰': 2,
    '叁': 3,
    '肆': 4,
    '伍': 5,
    '陆': 6,
    '柒': 7,
    '捌': 8,
    '玖': 9,

    '貮': 2,
    '两': 2,
}
CN_UNIT = {
    '十': 10,
    '拾': 10,
    '百': 100,
    '佰': 100,
    '千': 1000,
    '仟': 1000,
    '万': 10000,
    '萬': 10000,
    '亿': 100000000,
    '億': 100000000,
    '兆': 1000000000000,
}

#判断该汉字数字是否带有“十百千万...或者拾佰仟萬...”单位
def is123(list_cn):
    for i in list_cn:
        if (i in CN_UNIT):
            return 1


S = input("请输入：")


def isNumber(cn, false=None):
    try:
        # 判定输入的是否全为阿拉伯数字，如果是直接返回eval(cn)
        if cn.isdigit():
            return eval(cn)
        # 输入的不是全为阿拉伯数字
        else:
            # 判定输入的汉字是否为数字，如果不则会返回TypeError,ValueError错误 会跳转到except异常处理
            if cn.isnumeric():
                lcn = list(cn)
                unit = 0  # 当前的单位
                ldig = []  # 临时数组

                # 处理没有单位的汉字，如一二三
                if (is123(lcn) == None):
                    while lcn:
                        cndig = lcn.pop(0)
                        dig = CN_NUM.get(cndig)
                        ldig.append(dig)
                    return int("".join('%s' %id for id in ldig))
                else:
                    # 以“万”，“亿”，“兆”分隔成四位的汉字数字
                    while lcn:
                        cndig = lcn.pop()  # 弹出列表的最后一个元素

                        if cndig in CN_UNIT:
                            unit = CN_UNIT.get(cndig)
                            if unit == 10000:
                                ldig.append('w')  # 标示万位
                                unit = 1
                            elif unit == 100000000:
                                ldig.append('y')  # 标示亿位
                                unit = 1
                            elif unit == 1000000000000:  # 标示兆位
                                ldig.append('z')
                                unit = 1

                            continue

                        else:
                            dig = CN_NUM.get(cndig)

                            if unit:
                                dig = dig * unit
                                unit = 0

                            ldig.append(dig)

                    if unit == 10:  # 处理10-19的数字
                        ldig.append(10)

                    ret = 0
                    tmp = 0

                    while ldig:
                        x = ldig.pop()

                        if x == 'w':
                            tmp *= 10000
                            ret += tmp
                            tmp = 0

                        elif x == 'y':
                            tmp *= 100000000
                            ret += tmp
                            tmp = 0

                        elif x == 'z':
                            tmp *= 1000000000000
                            ret += tmp
                            tmp = 0

                        else:
                            tmp += x

                    ret += tmp
                    return ret
    except(TypeError, ValueError):
        return false


# 判定输入是否为汉字数字，如果是则输出“这是一个数字，<阿拉伯数字>”，否则输出“这不是一个数字”

if (isNumber(S)):
    print("这是一个数字，{:.2f}".format(isNumber(S)))
else:
    print("这不是一个数字")


