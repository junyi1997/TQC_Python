# -*- coding: utf-8 -*-
def compute():
    a=input()
    b=input()
    c=a.split(",")
    d=b.split(",")
    x=int(c[0])
    y=int(c[1])
    m=int(d[0])
    n=int(d[1])
    mol=(x*n)+(y*m)
    den=y*n
    i=1
    j=0
    for i in range(1,mol):
        if (mol % i == 0) and (den % i == 0):
            j=i
    print()           
compute()
