# -*- coding: utf-8 -*-

#最大值與最小值之差

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

'''
a=int(input())
for i in range(a):
    b=input()
    b=b.split(" ")
    c=list(map(eval,b))
    d=max(c)-min(c)
    print("{:.2f}".format(d))
    '''