#__author__ = 'tooweakchen'
#coding:utf-8

import simplejson as json
import re
import urllib2
import xlwt

def get_file(filename):
    with open(filename,'r') as fp:
        str=fp.read()

    #print str
    str1=json.JSONDecoder().decode(str) #将数据变成json格式
    return str1

def make_xls(d):
    tp=xlwt.Workbook()
    table=tp.add_sheet("student",cell_overwrite_ok=True)#这里是数据可以覆盖
    for n in range(len(d)):
        table.write(n,0,n+1)
        m=1
        for str2 in d[str(n+1)]:
            table.write(n,m,str2)
            m+=1
    tp.save('/home/tooweakchen/桌面/ceshi.xls')
    print "所有操作已经完成"
def main():
    filename='student.txt'
    d=get_file(filename)
    make_xls(d)

if __name__=='__main__':
    main()