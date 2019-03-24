# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:12:18 2018

@author: user

迴圈階乘計算
"""

num=int(input())
sum=1
for i in range(1,num+1):
    sum=sum*i
print(sum)