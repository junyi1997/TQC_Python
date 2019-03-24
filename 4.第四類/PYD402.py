# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:13:20 2018

@author: user

不定數迴圈-最小值
"""

a=[]
while True:
    num=eval(input())
    if num == 9999:
        break
    a.append(num)
print(min(a))