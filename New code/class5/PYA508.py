# -*- coding: utf-8 -*-
def compute():
    a=input()
   
    c=a.split(",")
    x=int(c[0])
    y=int(c[1])
    f=min(x,y)
    j=0
    for i in range(1,f):
        if (x % i == 0) and (y % i == 0):
            j=i
    print(j)           
compute()