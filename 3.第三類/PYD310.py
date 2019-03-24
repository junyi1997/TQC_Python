# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:12:54 2018

@author: user

迴圈公式計算
"""

a=int(input())
sum=0
for i in range(2,a+1):
    ans=1/((i-1)**0.5+(i**0.5))
    sum=sum+ans
print("{:.4f}".format(sum))