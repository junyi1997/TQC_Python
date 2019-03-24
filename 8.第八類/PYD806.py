# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:18:28 2018

@author: user

字元次數計算

"""

def compute(a,b):
    c=a.count(b)
    print("{:} occurs {:} time(s)".format(b,c))
a=input()
b=input()
compute(a,b)