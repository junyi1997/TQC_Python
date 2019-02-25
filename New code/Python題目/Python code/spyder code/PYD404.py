# -*- coding: utf-8 -*-
#106111123 / 吳驊涓
#第二題
"""
i=1
a=input()
while i <= len(a):
    print(a[-i],end="")
    i=i+1
"""
num=int(input())
if num >0:
    while num >0:    
        r=int(num % 10)
        print(r,end="")
        num=(num-r)/10
elif num == 0:
    print(0)


input()