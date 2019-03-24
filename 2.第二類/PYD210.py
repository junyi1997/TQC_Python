# -*- coding: utf-8 -*-

#三角形判斷

a=eval(input())
b=eval(input())
c=eval(input())
if (a+b>c) and ( a+c>b) and (b+c>a):
    print(a+b+c)
else:
    print("Invalid")  

