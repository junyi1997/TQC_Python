# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:19:26 2018

@author: user

資料計算

"""

data=[]
name=[]
weight=[]
height=[]
with open("read.txt","r",encoding="utf-8") as file:
    for data in file:
        print(data)
        data=data.split(" ")
        name.append(data[0])
        height.append(int(data[1]))
        weight.append(int(data[2]))
h_in=height.index(max(height))
w_in=weight.index(max(weight))
print("Average height: {:.2f}".format(sum(height)/len(height)))
print("Average weight: {:.2f}".format(sum(weight)/len(weight)))
print("The tallest is {:} with {:.2f}cm".format(name[h_in],height[h_in]))
print("The heaviest is {:} with {:.2f}kg".format(name[w_in],weight[w_in])) 