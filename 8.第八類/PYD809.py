# -*- coding: utf-8 -*-

#密碼規則

a=input()
x=0
y=0
for i in a:
    if i.isdigit():
        x+=1
    elif i.isalpha():
        y+=1
if (len(a)>=8) and (x>=1) and (y>=1):
    print("Valid password")
else:
     print("Invalid password")
        
