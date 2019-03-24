# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:16:50 2018

@author: user

串列數組轉換
"""
da=[]
while True:
    a=int(input())
    if a == -9999:
        break
    else:
        da.append(a)
print(tuple(da))
print("Length: {:}".format(len(da)))
print("Max: {:}".format(max(da)))
print("Min: {:}".format(min(da)))
print("Sum: {:}".format(sum(da)))
