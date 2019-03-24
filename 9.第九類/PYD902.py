# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:19:15 2018

@author: user

資料加總

"""

with open("read.txt","r",encoding="utf-8") as fd:
    data=fd.read()
    d_sp=data.split(" ")
    d_li=list(map(eval,d_sp))
    print(sum(d_li) )   