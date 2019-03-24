# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:12:04 2018

@author: user

迴圈倍數總和
"""
a=int(input())
i=1
sum=0
while i <= a:
    if (i % 5 == 0):
        sum=sum+i
    i=i+1
print(sum) 
