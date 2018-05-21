# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 14:38
# @Author  : QuietWoods
# @FileName: main.py
# @Software: PyCharm
# @Email    ：1258481281@qq.com
import sys
import model as sentsim
from csv_helper import Sentence


def parse_argument():
    if len(sys.argv) < 1:
        print(u"arguments needed")
    try:
        args = {'inputfile': sys.argv[1], 'outputfile': sys.argv[2]}
        return args
    except IndexError as e:
        print(e)
    return None


if __name__ == '__main__':
    # argus = parse_argument()
    argus = {'inputfile': 'data/test.csv', 'outputfile': 'output.csv'}
    input_file = argus['inputfile']
    output_file = argus['outputfile']
    samples = Sentence(input_file, output_file)
    predicts = []
    for sample in samples:
        sample = sample.split('\t')[:3]
        test = sentsim.SentenceSimilarity(sample[1], sample[2])
        result = test.result()
        sample.append(str(result[0]))
        predicts.append(sample)

    samples.list2csv(result=predicts)
    print('*******************end*******************')

