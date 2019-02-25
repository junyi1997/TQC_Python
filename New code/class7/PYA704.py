# -*- coding: utf-8 -*-
num=[]
while True:
    num1=int(input())
    if num1 == -9999:
        break
    num.append(num1)
num1=set(num)
print("Length:",len(num1))
print("Max:",max(num1))
print("Min:",min(num1))
print("Sum:",sum(num1))
   
