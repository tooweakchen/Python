#!/usr/bin/env python
# coding=utf-8

#Python正则表达式
#正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。
#re 模块使 Python 语言拥有全部的正则表达式功能

re.match函数
re.match尝试从字符串的开始匹配一个模式
函数语法：
re.match(pattern,string,flags=0)

函数参数说明:
    pattern 匹配的正则表达式
    string  要匹配的字符串
    flags       标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配

#匹配成功re.match方法返回一个匹配的对象，否则返回None。


