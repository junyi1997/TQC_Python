# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:17:07 2018

@author: user

集合條件判斷
"""

a=set()
while True:
    b=int(input())
    if b == -9999:
        break
    else:
        a.add(b)

print("Length: {:}".format(len(a)))
print("Max: {:}".format(max(a)))
print("Min: {:}".format(min(a)))
print("Sum: {:}".format(sum(a)))