#输入一个字符串，将其中大写字母转为小写，小写字母转为大写，
# 其他字符保持原样，输出转换后的字符串。

# 把输入中的大写字母转为小写，小写字母转为大写，其他字符原样输出
# 可用分支语句完成
s = input()
for c in s:
    if c.islower():
        print(c.upper(), end='')
    elif c.isupper():
        print(c.lower(), end='')
    else:
        print(c, end='')

# 可用以下一条语句完成
# print(''.join([i.lower() if i.isupper() else i.upper() for i in input()]))

# 也可用下述方法将转变后的字符先加入列表，再将列表中的字符拼接到一起输出
# import string
#
#
# def swap_case(s):
#     ls = []
#     for c in s:
#         if c in string.ascii_lowercase:
#             ls.append(c.upper())
#         elif c in string.ascii_uppercase:
#             ls.append(c.lower())
#         else:
#             ls.append(c)
#     return ''.join(ls)
#
#
# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)