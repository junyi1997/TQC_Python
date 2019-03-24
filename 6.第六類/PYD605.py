# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:16:09 2018

@author: user

成績計算
"""

data=[]

for i in range(10):
    num=eval(input())
    data.append(num)
dmax=max(data)
dmin=min(data)
data.remove(dmax)
data.remove(dmin)
    
print("{:}".format(sum(data)))
print("{:.2f}".format(sum(data)/len(data)))