#/usr/bin/env python
#coding=utf-8
import jieba
import sys
from model import SentenceSimilarity


def process(inpath, outpath):
    with open(inpath, 'r') as fin, open(outpath, 'w') as fout:
        similar = SentenceSimilarity()
        for line in fin:
            lineno, sen1, sen2 = line.strip().split('\t')
            words1= [ w for w in jieba.cut(sen1) if w.strip() ]
            words2= [ w for w in jieba.cut(sen2) if w.strip() ]
            union = words1 + words2
            same_num = 0
            for w in union:
                if w in words1 and w in words2:
                    same_num += 1
            tt = similar.result()
            if tt:
                fout.write(lineno + '\t1\n')
            else:
                fout.write(lineno + '\t0\n')


if __name__ == '__main__':
    process(sys.argv[1], sys.argv[2])
