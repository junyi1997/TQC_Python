# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:16:21 2018

@author: user

成績計算
"""

data=[]
a=["1st","2nd","3rd"]
for i in range(3):
    data.append([])
    print("The {:} student:".format(a[i]))
    for j in range(5):
        data[i].append(eval(input()))


for j in range(3):
    print("Student {:}".format(j+1))
    print("#Sum {:}".format(sum(data[j])))
    print("#Average {:.2f}".format(sum(data[j])/len(data[j])))