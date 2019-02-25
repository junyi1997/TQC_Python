# -*- coding: utf-8 -*-
a=int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print("{:>4d}".format(i*j),end="")
    print("")
