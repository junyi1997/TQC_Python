# -*- coding: utf-8 -*-
a=eval(input())
b=eval(input())
c=eval(input())
if a+b>=c:
    print(a+b+c)
elif a+c >=b:
    print(a+b+c)
elif b+c >=a:
    print(a+b+c)
else:
    print("Invalid")
#a=[]
#for i in range(3):
#    a.append(int(input()))
#b=a.sort()
#print(a)
#print(b)
#type(b)