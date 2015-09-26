#!/usr/bin/env python
# coding=utf-8

#不可变序列-----元组 tuple 
#就是不能修改
#比如：user=(1,2,3)
#user[0]=2这是会报错的
#创建元组
tuple_name=()

(4)
4
(4,)
(4,)

#元组中元素去重
set((2,2,2,4,4))
set([2,4])

zoo=('a','b','c','d')
#求元组内的个数
print len(zoo)
4

#排序，从小到大
zoo=(1,3,4,2)
a,b,c,d=sorted(zoo)
1,2,3,4


new_zoo=('A','B','C','D',zoo)
print len(new_zoo)
5

print new_zoo[2]
C

print new_zoo[4][1]
b

#解包
user=(1,2,3)
a,b,c=user
a=1,b=2,c=3


