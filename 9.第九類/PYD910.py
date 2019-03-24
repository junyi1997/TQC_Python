# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:19:58 2018

@author: user

學生基本資料

"""

f_name = "read.dat"
with open(f_name,"r",encoding="utf-8") as fd:
    title=fd.readline()
    print(title)
    gender={"1":0,"0":0}
    for d in fd:
        print(d)
        da=d.split(" ")
        gender[da[2]]+=1
print("Number of males: {:}".format(gender["1"]))
print("Number of females: {:}".format(gender["0"]))