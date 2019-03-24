# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:19:36 2018

@author: user

字串資料取代

"""

f_name = input()
str_old = input()
str_new = input()
with open(f_name,"r",encoding="utf-8") as fd:
    data=fd.read()
print("=== Before the replacement")
print(data)
data=data.replace(str_old,str_new)
print("=== After the replacement")
print(data)