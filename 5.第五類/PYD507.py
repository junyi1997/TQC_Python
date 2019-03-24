# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:15:16 2018

@author: user

質數

"""

def compute(x):
    i=2
    while i < x:      
        if (x%i)==0:
            return False
        i+=1
    return True
x=int(input())
if x <= 1:
    print("Not Prime")
elif x == 2:
    print("Prime")
else:
    r=compute(x)
    if r ==True:
        print("Prime")
    else:
        print("Not Prime")