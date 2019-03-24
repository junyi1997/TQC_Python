# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:18:01 2018

@author: user

字元對應

"""

val=input()
sum=0
for i in range(len(val)):
    ordv=ord(val[i])
    sum+=ordv
    print("ASCII code for '{:}' is {:}".format(val[i],ordv))
print(sum)