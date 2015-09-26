#__author__ = 'tooweakchen'
# -*- coding=utf-8 -*-
#你有一个目录，放了你一个月的日记，都是 txt，
# 为了避免分词的问题，假设内容都是英文，
# 请统计出你认为每篇日记最重要的词
#
import re
import glob

def get_list():
    file=glob.glob(r'/home/tooweakchen/文档/测试/*.txt')
    #print file
    return file

def get_str(address):
    f=open(address,'rb')
    word=f.read()
    return word


def count_chr(str1):
    list2=re.findall(r'[a-zA-Z]+\b',str1)
    return list2

def count(str2):
    str_dict={}
    list3=count_chr(str2)
    print list3
    for item in list3:
        if item in str_dict:
            #print "YESYESYES"
            str_dict[item]+=1
        else:
            str_dict[item]=1
    max1=0
    for key,value in str_dict.items():
        #print key,value
        #print type(value)
        max1=max(max1,value)
    time= max1
    for key,value in str_dict.items():
        if value == max1:
             words=key
             break
    #for key,value in str_dict.items():
     #   print 'key=',key, 'value=',value
    #time=str_dict[max(str_dict)]
    #words=max(str_dict)
    #str_dict = {str_dict[key]:key for key in str_dict}
    #print str_dict
    #print max(str_dict)
    #print str_dict[max(str_dict)]
    #temp={}
    #for key in str_dict:
        #print key
    #    temp[str_dict[key]]=key
     #   print temp[str_dict[key]],temp

    #print max(temp)
    print '出现最多的单词为' + str(words) + '，出现了' + str(time) + '次'


def main():
    list1=get_list()
    for list in list1:
        str2=get_str(list)
        count(str2)



if __name__=='__main__':
    main()