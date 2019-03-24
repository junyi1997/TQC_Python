# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:19:47 2018

@author: user

單字次數計算

"""

f_name = input()
n = int(input())
nl=[]
wcom={}
with open(f_name,"r",encoding="utf-8")as fd:
    data=fd.read()
    data=data.split()
    for k in data:
        if k in wcom:
            wcom[k]+=1
        else:
            wcom[k]=1
for k in wcom:
    if wcom[k]==n:
        nl.append(k)
nl.sort()
for i in range(len(nl)):
    print(nl[i])