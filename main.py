# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 14:38
# @Author  : QuietWoods
# @FileName: main.py
# @Software: PyCharm
# @Email    ：1258481281@qq.com
import sys


def parse_argument():
    print(sys.argv[:])
    if len(sys.argv) < 1:
        print(u"arguments needed")
    try:
        args = {'inputfile': sys.argv[1], 'outputfile': sys.argv[2]}
        return args
    except IndexError as e:
        print(e)
    return None


parse_argument()
