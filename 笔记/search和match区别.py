#!/usr/bin/env python
# coding=utf-8

match()函数只检测RE是不是在string的开始位置匹配
search()会扫描整个string查找匹配
也就是说match()只有在0位置匹配成功的话才有返回，
如果不是开始位置匹配成功的话，match()就返回none。

例如：
print (re.match('super','superstition').span()) 

会返回(0,5)

而print (re.match('super','insuperstition').span())
则返回None

search()会扫描整个字符串并返回第一个成功的匹配
例如：
print (re.search('super','superstition').span())
会返回（0,5）

print (re.search('super','insuperstition').span())
则会返回(2,7)

#顺便这里提一下span()函数
#返回一个元组包含匹配 (开始,结束) 的位置
#
