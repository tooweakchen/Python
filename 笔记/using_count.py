#!/usr/bin/env python
# coding=utf-8

# Python count()方法
# python count()方法用于统计字符串里某个字符出现的次数。可选
#参数为在字符串搜索的开始和结束的位置

#语法
count()方法语法：
str.count(sub,start=0,end=len(str))

#参数
1. sub -- 搜索的子字符串
2. start -- 字符串开始搜索的位置。默认为第一个字符，第一个字符索引值为0
3. end --字符串中结束搜索的位置。字符中第一个字符的索引为0.默认为字符串的最后一个位置

#返回值
该方法返回子字符串在字符串中出现的次数

#实例

str="this is string eample ...wow!!!"
sub="i"
print "str.count(sub,4,40):",str.count(sub,4,40)
结果是:str.count(sub, 4, 40): 2
sub="wow"
print "str.count(sub) : ", str.count(sub)
结果是：str.count(sub) : 1


