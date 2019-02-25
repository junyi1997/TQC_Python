# -*- coding: utf-8 -*-
def compute():
    x=int(input())
    y=int(input())
    sum=0
    while x <=y:
        sum=sum+x
        x=x+1
    print(sum)
    return sum

compute()
