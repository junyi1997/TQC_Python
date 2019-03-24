# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:16:56 2018

@author: user

 數組合併排序
"""

b1=()
b2=()
print("Create tuple1:")
while True:
    a1=int(input())
    if a1 == -9999:
        break
    else:
        b1=b1+(a1,)
print("Create tuple2:")
while True:
    a2=int(input())
    if a2 == -9999:
        break
    else:
        b2=b2+(a2,)

print("Combined tuple before sorting: {:}".format(b1+b2))
t=list(b1+b2)
t.sort()
print("Combined list after sorting: {:}".format(t))