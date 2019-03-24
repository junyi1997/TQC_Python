# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:13:26 2018

@author: user

倍數總和計算

"""

a=int(input())
b=int(input())
c=[]
j=0
sum=0
while a <= b:
    if (a % 4 == 0) or (a % 9 == 0):
        c.append(a)
        sum=sum+a
    a=a+1
for i in c:
    j=j+1
    print("{:<4}".format(i),end="")
    if j % 10 == 0:
        print("")
print("") 
print(len(c))   
print(sum)