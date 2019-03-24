# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:15:05 2018

@author: user

依參數格式化輸出

"""

def compute():
    a=input()
    x=int(input())
    y=int(input())
    for i in range(y):
        for j in range(x):
            print(a,end=" ")
        print("")
compute()