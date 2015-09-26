#__author__ = 'tooweakchen'
# coding=utf-8
# 做为 Apple Store App 独立开发者，你要搞限时促销，
# 为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）？

import random,string

def rndom(num,length):
    file=open("/home/tooweakchen/文档/代码/随机数.txt","wb")
    str1=string.letters+string.digits
    for i in range(num):
        s=[random.choice(str1) for i in range(length)]
        file.write(''.join(s)+'\n')
    file.close()

if __name__=='__main__':
    rndom(200,7)
