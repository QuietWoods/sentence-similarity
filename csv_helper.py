# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 14:23
# @Author  : QuietWoods
# @FileName: csv_helper.py
# @Software: PyCharm
# @Email    ：1258481281@qq.com
#!/usr/bin/env python
import os
import csv
from distutils.log import warn as printf


class Sentence:
    def __init__(self, input_file, output_file):
        self.fname = input_file
        self.output_file = output_file

    def __iter__(self):
        with open(self.fname, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                yield row[0]

    def list2csv(self, result):
        with open(self.output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for i, item in enumerate(result):
                if item:
                    writer.writerow(['\t'.join(item)])

