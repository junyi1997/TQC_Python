# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:17:24 2018

@author: user

共同科目
"""

x=set()
y=set()
print("Enter group X's subjects:")
while True:
    a=input()
    if a == "end":
        break
    else:
        x.add(a)
print("Enter group Y's subjects:")
while True:
    a=input()
    if a == "end":
        break
    else:
        y.add(a)
z1=list(x|y)
z2=list(x&y)
z3=list(y-x)
z4=list((x|y)-(x&y))
z1.sort()
z2.sort()
z3.sort()
z4.sort()
print(z1)
print(z2)
print(z3)
print(z4)