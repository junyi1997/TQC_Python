# -*- coding: utf-8 -*-
#最大公因數

def compute():
    n=input()
    a=n.split(",")
    x=int(a[0])
    y=int(a[1])
    nmin=min(x,y)
    j=0
    for i in range(1,nmin+1):
        if (x % i == 0) and (y % i == 0):
            j=i
    print(j)
compute()