
# coding:utf-8

#第 0008 题：一个HTML文件，找出里面的正文
from pyquery import PyQuery as pq
import urllib2
import re
from lxml import etree

def get_html(url):
    html=urllib2.urlopen(url).read()
    return html

def get_html1(html):
    zhengze=r'<div class="content">([^$]*)<div class="article-copyright">'
    match=re.search(zhengze,html)
    html=match.group(1)
    return html

def get_result(html):
    #这里是解码，因为有中文，怕出现乱码，直接统一解码成utf-8
    html=html.decode('utf-8')
    d=pq(html)
    l=d('p')
    #print l.text()
    list1=[]
    for str in l:
        list1.append(pq(str).text())

    return list1

def main():
    url='http://jimmy66.com/164.html'
    html=get_html(url)
    html1=get_html1(html)
    list1=get_result(html1)
    for line in list1:
        print line

if __name__=='__main__':
    main()
