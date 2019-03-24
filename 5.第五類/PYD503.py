# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:14:48 2018

@author: user

連加計算

"""

def compute(a,b):
    sum=0
    for i in range(a,b+1):
        sum+=i
    print(sum)
a=int(input())
b=int(input())
compute(a,b)