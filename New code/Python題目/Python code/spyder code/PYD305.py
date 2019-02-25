# -*- coding: utf-8 -*-
#數字
num=eval(input())
while num > 0:
    r=int(num % 10)
    print(r,end="")
    num=(num-r)/10

#字串
num=input()
i=len(num)-1
while i >= 0:
    print(num[i],end="")
    i=i-1