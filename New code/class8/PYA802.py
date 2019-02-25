# -*- coding: utf-8 -*-
#ord
a=input()
sum=0
for i in a:
    ordi=ord(i)
    sum+=ordi
    print("ASCII code for '{:}' is {:}".format(i,ordi))
    print(sum)