# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:14:12 2018

@author: user

得票數計算

"""

Nami=0
Chopper=0
scrap=0
for i in range(5):
    poll=int(input())
    if poll ==1:
        Nami=Nami+1
    elif poll ==2:
        Chopper=Chopper+1
    else:
        scrap=scrap+1
    print("Total votes of No.1: Nami = ",Nami)