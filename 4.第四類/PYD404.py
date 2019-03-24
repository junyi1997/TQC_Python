# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:13:33 2018

@author: user

數字反轉判斷

"""

num=int(input())
if num==0:
    print(0)
else:
    while num >0:
        r=int(num%10)
        print(r,end="")
        num=(num-r)/10
    print("")