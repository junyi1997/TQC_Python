# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:14:20 2018

@author: user

繪製等腰三角形

"""

fool=int(input())
for i in range(1,fool+1):
    for j in range(fool-i):
        print(" ",end="")
    for k in range(i*2-1):
        print("*",end="")
    print("")