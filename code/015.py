#__author__ = 'tooweakchen'
#coding:utf-8

import simplejson as json
import xlwt

def get_file(filename):

    with open(filename,'r') as fp:
        str=fp.read()

    d=json.JSONDecoder().decode(str)
    return d

def make_xls(d):
    tp=xlwt.Workbook()
    table=tp.add_sheet('city',cell_overwrite_ok=True)
    for n in range(len(d)):
        table.write(n,0,n+1)
        table.write(n,1,d[str(n+1)])


    tp.save('/home/tooweakchen/文档/代码/city.xls')
    print "所有操作已经完成"

def main():
    filename='city.txt'
    d=get_file(filename)
    make_xls(d)

if __name__=='__main__':
    main()