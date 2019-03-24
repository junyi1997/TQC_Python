# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:11:35 2018

@author: user

迴圈偶數連加
"""

a=int(input())
b=int(input())
i=a
sum=0
while i <= b:
    if (i % 2 == 0):
        sum=sum+i
    i=i+1
print(sum)     