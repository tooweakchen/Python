#!/usr/bin/env python
# coding=utf-8

#python如何实现文件的下载

#方法一

代码如下:
    import os #这是引入操作系统的模块
    import re
    import urllib2

    path='/home/tooweakchen/桌面/picture/'
    os.mkdir(path) #在指定位置新建一个名叫picture的文件夹
    os.chdir(path) #指定文件下载到哪里
    url="http://........"  #下载链接
    
    print "downloading with urllib2"
    response=urllib2.urlopen(url)
    data=response.read()
    filname='xxx' #下载后保存的文件名
    with open(filname,"wb") as fp:
        fp.write(data)



