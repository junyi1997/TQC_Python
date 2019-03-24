# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:19:08 2018

@author: user

成績資料

"""

with open("write.txt","w",encoding="utf-8") as fd:
    for i in range(5):
        fd.write(input())
        if i != 4:
            fd.write("\n")