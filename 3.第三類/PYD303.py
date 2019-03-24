# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:11:40 2018

@author: user

迴圈數值相乘
"""

a=int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print("{:>4d}".format(i*j),end="")
    print("")