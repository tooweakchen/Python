#!/usr/bin/env python
# coding=utf-8

#全局变量global的使用

def func():
        global x

            print 'x is', x
                x = 2
                    print 'Changed local x to', x

 x = 50
 func()
 print 'Value of x is', x

 #结果如下：

 x is 50
 Changed local x to 2

 Value of x is 2

 #如果没有global x这语句，那么这运行会报错的，因为x一开始没有被赋值
