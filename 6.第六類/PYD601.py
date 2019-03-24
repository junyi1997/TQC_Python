# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:15:46 2018

@author: user

偶數索引值加總

"""
data=[]
sum=0
for i in range(12):
    data.append(int(input()))
k=0
for j in data:
    print("{:>3}".format(j),end="")
    if (k % 2)==0:
        sum+=data[k]
    k+=1
    if (k % 3)==0:
        print("") 
print(sum)
