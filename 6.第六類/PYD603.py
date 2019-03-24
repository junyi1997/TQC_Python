# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:15:59 2018

@author: user

數字排序

"""

data=[]
for i in range(10):
    data.append(int(input()))
data.sort()
d=data[-3:]
#dm=d[::-1]
#for i in dm:
print(d[2],d[1],d[0])