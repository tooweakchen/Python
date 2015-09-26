#__author__ = 'tooweakchen'
#coding:utf-8

#第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，
# 否则打印出 Human Rights。
def get_list():
    list1=[]
    filepath="/home/tooweakchen/文档/mingan.txt"
    f=open(filepath,"r")
    s=f.readlines()
    for str in s:
        #print str
        list1.append(str.strip())
    #print list1
    f.close()
    return list1

def output(str):
    list1=get_list()
    if str in list1:
        print "Freedom"
    else:
        print "Human Rights"

def main():
    str=raw_input()
    output(str)

if __name__=='__main__':
    main()