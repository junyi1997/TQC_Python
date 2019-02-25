# -*- coding: utf-8 -*-
fool=int(input())
for i in range(1,fool+1):
    for j in range(fool-i):
        print(" ",end="")
    for k in range(i*2-1):
        print("*",end="")
    print("")
