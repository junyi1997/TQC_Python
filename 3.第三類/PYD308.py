# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:12:28 2018

@author: user

 迴圈位數加總
"""

floor=int(input())
sum=0
for i in range(floor):
    num=int(input())
    copy=num
    sum=0    
    while num > 0:
        r=int(num%10)
        sum=sum+r
        num=(num-r)/10
    
    print("Sum of all digits of {:} is {:}".format(copy,sum))