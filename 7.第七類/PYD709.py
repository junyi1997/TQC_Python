# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:17:38 2018

@author: user

詞典排序

"""

c={}
while True:
   key = input("Key: ")
   if key =="end":
       break
   else:
       value = input("Value: ")
       c[key]=value
d=list(c.keys())
d.sort()
for i in d:
    print("{:}: {:}".format(i,c[i]))