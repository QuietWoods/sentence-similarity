# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 14:38
# @Author  : QuietWoods
# @FileName: main.py
# @Software: PyCharm
# @Email    ：1258481281@qq.com
import sys


def parse_argument():
    if len(sys.argv) < 1:
        print(u"arguments needed")
    try:
        args = {'inputfile': sys.argv[0], 'outputfile': sys.argv[1]}
        return args
    except IndexError as e:
        print(e)
    return None


if __name__ == '__main__':
    # 得到shell命令中的参数
    argus = parse_argument()
    print(argus)

