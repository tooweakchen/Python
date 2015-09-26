#__author__ = 'tooweakchen'
#coding:utf-8

#敏感词文本文件 filtered_words.txt，里面的内容
#  和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，
# 例如当用户输入「北京是个好城市」，则变成「**是个好城市」
import re

#读取文件，并且以列表的形式返回
def get_list(filepath):
    list1=[]
    f=open(filepath,'r')
    s=f.readlines()
    for str in s:
        list1.append(str.strip())#这里利用strip()把换行符去掉了
    return list1

    #return list1

def output():
    filepath='/home/tooweakchen/文档/mingan.txt'
    list1=get_list(filepath)
    str2=''
    #复习了切片
    #生成相对应的正则表达式
    for str1 in list1:
        str2+=str1+'|'
    str2=str2[:-1]
    #print str2
    str=raw_input()
    print re.sub(str2,'**',str)#这里如果指定了str2=abc的话，那就可以直接re.sub(r'abc','**',str)


def main():
    output()


if __name__=='__main__':
    main()
