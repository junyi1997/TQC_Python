# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:19:53 2018

@author: user

聯絡人資料

"""

with open("data.dat","w",encoding="utf-8") as fd:
    for i in range(5):
        fd.write(input())
        fd.write("\n")
        if i <4:
            fd.write("\n")

with open("data.dat","r",encoding="utf-8") as fd:
    print("The content of \"data.dat\":")
    data=fd.read()
    print(data)