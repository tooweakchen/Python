#__author__ = 'tooweakchen'
#coding=utf-8

#第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
# 包括空行和注释，但是要分别列出来
import glob
import re
def get_filelist(filepath):
    filelist=glob.glob(filepath)
    return filelist

def count_(filepath):
    filelist=get_filelist(filepath)
    #print filelist
    for filename in filelist:
        n1=n2=0
        f=open(filename,'rb')
        #这里不能用read（），不然等下就是一个单词一个单词的统计
        #用readlines（）是一行一行的读取，符合要求
        linelist=f.readlines()
        print linelist
        for str in linelist:
            #这里匹配以#开始的注释行
            if re.match(r'#',str)!=None:
                n1+=1
            #这里匹配以无限个或者多个空格开始最后以换行结束的空白行
            elif re.match(r' *\n',str)!=None:
                n2+=1
        print "%d 总行数"%(len(linelist))
        print "%d 行注释"%(n1)
        print "%d 行空白"%(n2)
        print "%d 行代码"%(len(linelist)-n1-n2)

if __name__=='__main__':
    filepath="/home/tooweakchen/文档/测试/*.txt"
    count_(filepath)
