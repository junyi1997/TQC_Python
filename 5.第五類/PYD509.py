# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:15:28 2018

@author: user

最簡分數

"""

def compute(p,q):
    f=max(p,q)
    j=0
    for i in range(1,f):
        if (p % i == 0) and (q % i == 0):
            j=i
    print("{:}/{:} + {:}/{:} = {:.0f}/{:.0f}".format(x,y,m,n,p/j,q/j))

a=input()
b=input()
c=a.split(",")
d=b.split(",")
x=int(c[0])
y=int(c[1])
m=int(d[0])
n=int(d[1])
p=x*n+y*m
q=y*n
compute(p,q)
