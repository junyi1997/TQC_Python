# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:16:04 2018

@author: user

眾數

"""

data=[]
numcount=0
numna=0
for i in range(10):
    data.append(int(input()))
ds=set(data)
for ev in ds:
    num=data.count(ev)
    if num>numcount:
        numcount=num
        numna=ev
print(numna)
print(numcount)