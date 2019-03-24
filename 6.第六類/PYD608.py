# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:16:26 2018

@author: user

最大最小值索引

"""

data=[]
d_max=0
d_min=99999
for i in range(3):
    data.append([])
    for j in range(3):
        num=eval(input())
        data[i].append(num)
        if num > d_max:
            d_max=num
            d_ind=(i,j)
        if num < d_min:
            d_min=num
            da_ind=(i,j)
print("Index of the largest number {:} is: ({:}, {:})".format(d_max,d_ind[0],d_ind[1]))
print("Index of the smallest number {:} is: ({:}, {:})".format(d_min,da_ind[0],da_ind[1]))