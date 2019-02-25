# -*- coding: utf-8 -*-
a=int(input())
while a > 0:
    r=int(a%10)
    print(r,end="")
    a=(a-r)/10
print("")
    
