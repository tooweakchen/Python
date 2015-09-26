#!/usr/bin/env python
# coding=utf-8

#计算n!最后有多少个连续的0

代码如下：

sum=0

while(n>=5):
    n/=5
    sum+=n

return sum
