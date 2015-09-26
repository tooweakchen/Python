#__author__ = 'tooweakchen'
#coding:utf-8

import simplejson as json
import xlwt

def get_file(filename):
    with open(filename,'r') as fp:
        str1=fp.read()

    data=json.JSONDecoder().decode(str1)
    return data

def make_xls(data):
    tp=xlwt.Workbook()
    table=tp.add_sheet('numbers',cell_overwrite_ok=True)
    for n in range(len(data)):
        m=0
        for str1 in data[n]:
            table.write(n,m,str1)
            m+=1

    tp.save('numbers.xls')
    print "所有操作已经完成"

def main():
    filename='numbers.txt'
    data=get_file(filename)
    make_xls(data)

if __name__=='__main__':
    main()