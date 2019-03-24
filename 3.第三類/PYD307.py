# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:12:23 2018

@author: user

乘法表
"""

j=int(input())
for a in range(1,j+1):
    for b in range(1,j+1):
        print("{:<2d}* {:<2d}= {:<4d}".format(b,a,b*a),end="")
    print("")