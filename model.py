# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 19:57
# @Author  : QuietWoods
# @FileName: model.py
# @Software: PyCharm
# @Email    ：1258481281@qq.com
import numpy as np


class SentenceSimilarity:
    def __init__(self, sent1, sent2):
        self.sent1 = sent1
        self.sent2 = sent2

    def result(self):
        result = np.random.randint(0, 2, 1)
        return list(result)
