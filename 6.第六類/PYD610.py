# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:16:38 2018

@author: user

平均溫度

"""

d=[]
h=0
l=999999
sum=0
k=0
for i in range(4):
    print("Week {:}:".format(i+1))
    d.append([])
    for j in range(3):
        k+=1
        print("Day {:}:".format(j+1),end="")
        num=eval(input())
        d[i].append(num)
        sum+=num
        if num > h:
            h=num
        if num < l:
            l= num

print("Average: {:.2f}".format(sum/k))
print("Highest: {:}".format(h))
print("Lowest: {:}".format(l))