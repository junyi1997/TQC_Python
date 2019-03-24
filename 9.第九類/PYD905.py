# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:19:31 2018

@author: user

字串資料刪除

"""

f_name = input()
string = input()
with open(f_name,"r",encoding="utf-8") as fd:
    data=fd.read()
    print("=== Before the deletion")
    print(data)
    data=data.replace(string,"")
print("=== After the deletion")
print(data)