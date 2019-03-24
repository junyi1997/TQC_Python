# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:12:12 2018

@author: user

數字反轉
"""

a=int(input())
while a > 0:
    r=int(a%10)
    print(r,end="")
    a=(a-r)/10
print("")