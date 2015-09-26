#__author__ = 'tooweakchen'
# -*- coding: utf-8 -*-

#第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
#正则表达式操作
import re

def count_test(filepath):
    file=open(filepath,'rb')
    s=file.read()
    word=re.findall(r'[a-zA-Z0-9]+',s)
    print word
    return len(word)

if __name__=='__main__':
    num=count_test("/home/tooweakchen/文档/代码/count_test.txt")
    print num