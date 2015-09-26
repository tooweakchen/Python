#__author__ = 'tooweakchen'
#coding:utf-8
import re
import urllib2

#第 0009 题：一个HTML文件，找出里面的链接
#获得网页源代码，但是不能直接用urllib2.urlopen(url)
#因为这样href="/opensearch.xml"等下就无法匹配了

#读取文件
def get_html():
    req=urllib2.Request('file:/home/tooweakchen/文档/Show-Me-the-Code_show-me-the-code.html')
    html=urllib2.urlopen(req).read()
    return html

def get_href(html):
    #这里加括号的可以直接取出来
    list1=re.findall(r'href="(http[s]?:[^"]+)"',html)
    return list1

def main():
    html=get_html()
    list1=get_href(html)
    for str in list1:
        print str

if __name__=='__main__':
    main()