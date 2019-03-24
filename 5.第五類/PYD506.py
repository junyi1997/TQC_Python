# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:15:11 2018

@author: user

一元二次方程式

"""

def compute():
    a=eval(input())
    b=eval(input())
    c=eval(input())
    x1=0
    x2=0
    if (b**2)-(4*a*c)<0:
        print("Your equation has no root.")
    else:
        x1=((-1*b)+(b**2-4*a*c)**0.5)/(2*a)
        x2=((-1*b)-(b**2-4*a*c)**0.5)/(2*a)
        print("{:}, {:}".format(x1,x2))
compute()