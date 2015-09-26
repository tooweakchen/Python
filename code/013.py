#__author__ = 'tooweakchen'
#coding:utf-8

import re
import urllib2
import os

def get_html(url):
    req=urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36')
    html=urllib2.urlopen(req).read().decode('utf-8')
    return html

def get_url_list(html):
    #r'src="(.*?\.jpg)" bdwater='
    l=re.findall(r'src="(http://.*?\.jpg)" bdwater=',html)
    return l

def get_imge(url):
    html=urllib2.urlopen(url)
    data=html.read()
    return data

def img_save(url,num):
    num = str(num)
    print '正在抓取第',num,'张'
    filename = num + '.jpg'
    with open(filename,'wb') as fp:
        data=get_imge(url)
        fp.write(data)

def main():
    url="http://tieba.baidu.com/p/2166231880"
    html=get_html(url)
    url_list=get_url_list(html)
    flag=0
    path='/home/tooweakchen/桌面/ceshi'
    if flag==0:
        os.mkdir(path)
        os.chdir(path)
        flag=1
    num=0
    for list1 in url_list:
        num+=1
        img_save(list1,num)


if __name__=='__main__':
    main()