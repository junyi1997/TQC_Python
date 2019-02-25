# -*- coding: utf-8 -*-
a=int(input())
b=int(input())
i=a
sum=0
while i <= b:
    if (i % 2 == 0):
        sum=sum+i
    i=i+1
print(sum)        