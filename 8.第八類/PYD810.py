# -*- coding: utf-8 -*-
a=int(input())
for i in range(a):
    n=input()
    data=[]
    da=n.split()
    
    damax=0
    damin=99999
    for j in range(len(da)):
        if damax < eval(da[j]):
            damax=eval(da[j])
        elif damin > eval(da[j]):
            damin=eval(da[j])
    daval=damax-damin
    print("{:.2f}".format(daval))
