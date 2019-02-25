# -*- coding: utf-8 -*-
num=int(input())
if num==0:
    print(0)
else:
    while num >0:
        r=int(num%10)
        print(r,end="")
        num=(num-r)/10
    print("")
