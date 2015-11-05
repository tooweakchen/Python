#__author__ = 'tooweakchen'
#coding:utf-8

import re

def count(filepath):
    with open(filepath,'r') as f:
        s=f.read()
    flag=0
    str1=""
    list2=[]
    flag1=0
    '''
    这里追加需求：引号内元素需要算作一个单词
    '''
    for i in range(len(s)):
        if (s[i]>='a' and s[i]<='z') or (s[i]>='A' and s[i]<='Z'):
            str1+=s[i]
        elif flag1==0 and (s[i]=='"' or s[i]=="'"):
            list2.append(str1)
            flag1=1
            flag=1
            str1=""
        elif flag1==1 and (s[i]=='"' or s[i]=="'"):
            list2.append(str1)
            str1=""
            flag1=0
            flag=0
        elif s[i]==' ' and flag==1:
            continue
        elif s[i]==' ' and flag==0:
            list2.append(str1)
            str1=""
        elif i==len(s):
            list2.append(str1)
    '''
    list1=re.findall(r'[a-zA-Z]+',s) #这是一种在文章中提取出所有的英文单词！！
    '''
    dict1={}
    for str in list2:
        if dict1.has_key(str):
            dict1[str]+=1
        else:
            dict1[str]=1
    print dict1
    sort=sorted(dict1.items(),key=lambda e:e[1],reverse=True)  #按照值来排序，从大到小
    for i in range(10):
        print sort[i]
    sort1=sorted(dict1.items(),key=lambda e:e[0],reverse=False) #按照健来排序，从小到大
    print sort1

if __name__=='__main__':
    filepath="/home/tooweakchen/桌面/words.txt"
    count(filepath)
