# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:17:43 2018

@author: user

詞典搜尋

"""

d={}
while True:
    key = input("Key: ")
    if key == "end":
        break
    else:
        value = input("Value: ")
        d[key]=value
c=input("Search key: ")
e=d.keys()
if c in e:
    print("True")
else:
    print("False") 