#!/usr/bin/env python
# coding=utf-8

# python中set（）是一个 基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算.（里面存的一定是不重复的元素）

s="The quick, brown fox jumps over the lazy dog!"
x=set(s)
print x
set(['!', ' ', ',', 'a', 'c', 'b', 'e', 'd', 'g', 'f', 'i', 'h', 'k', 'j', 'm', 'l', 'o', 'n', 'q', 'p', 's', 'r', 'u', 't', 'w', 'v', 'y', 'x', 'z'])

basket= [’apple’, ’orange’, ’apple’, ’pear’, ’orange’, ’banana’]
y=set(basket)
print y
set([’orange’, ’pear’, ’apple’, ’banana’])

'orange' in y
True

a = set(’abracadabra’)
b = set(’alacazam’)
print a
set([’a’, ’r’, ’b’, ’c’, ’d’])

print a-b #letters in a but not in b
set(['r','d','b'])

print a|b # letters in either a or b
set([’a’, ’c’, ’r’, ’d’, ’b’, ’m’, ’z’, ’l’])

print a&b #letters in both a and b
set([’a’, ’c’])

print a^b # letters in a or b but not both
set([’r’, ’d’, ’b’, ’m’, ’z’, ’l’])

print len(a)
5

#测试是否 s 中的每一个元素都在 t 中
s.issubset(t)
s <= t
#测试是否 t中的每一个元素都在 s中
s.issuperset(t)
t<=s

#返回一个新的 set 包含 s 和 t 中的每一个元素
s.union(t)
s|t

#返回一个新的 set 包含 s 和 t 中的公共元素
s.intersection(t)
s&t

#返回一个新的 set 包含 s 中有但是 t 中没有的元素
s.difference(t)
s-t

#向set "s"中添加元素x
s.add(x)

#从set "s"中删除元素x，如果不存在则引发keyError
s.remove(x)

#删除并且返回set "s"中一个不确定的元素，
#如果为空则引发keyError
s.pop()

#删除set "s"中的所有元素
s.clear()


