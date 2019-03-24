# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:17:02 2018

@author: user

數組條件判斷

"""

d=[]
while True:
    a=input()
    if a == "end":
        break
    else:
       d.append(a)
print(tuple(d))
print(tuple(d[:3]))
print(tuple(d[-3:]))