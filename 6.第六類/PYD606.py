# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:16:15 2018

@author: user

二維串列行列數

"""

def compute(): 
    r=int(input())
    c=int(input())
    for i in range(r):
        for j in range(c):
            print("{:4}".format(j-i),end="")
        print("")
compute()